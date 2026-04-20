#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import shutil
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, StrictUndefined

ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = ROOT / "corpus"
GUIDELINES_DIR = CORPUS_DIR / "guidelines"
COLUMNS_PATH = CORPUS_DIR / "columns" / "columns.yml"
TEMPLATES_DIR = ROOT / "templates"
BUILD_EVIDENCE_DIR = ROOT / "build" / "evidence"
SITE_PUBLIC_EVIDENCE_DIR = ROOT / "site" / "public" / "evidence"

SAMD_COLUMNS = ["A", "B", "G", "K", "M"]
SAMD_GUIDELINES = [
    ("pmda-samd", "PMDA"),
    ("fda-aiml-saamd-ap", "FDA"),
    ("eu-ai-act", "EU"),
    ("who-aih", "WHO"),
    ("nist-ai-rmf", "NIST"),
]
PCCP_COLUMNS = ["G", "F", "L"]
PCCP_GUIDELINES = [
    ("fda-aiml-saamd-ap", "FDA"),
    ("pmda-samd", "PMDA"),
    ("eu-ai-act", "EU"),
]
IRB_COLUMNS = ["A", "B", "C", "F", "D", "H", "I", "L"]
IRB_GUIDELINES = [
    ("who-aih", "WHO AIH"),
    ("nist-ai-rmf", "NIST AI RMF"),
    ("jmsf-ai-medical", "JMSF"),
]
CLINICAL_AI_PRODUCT_COLUMNS = ["A", "B", "C", "F", "D", "H", "I", "J", "L", "M"]
CLINICAL_AI_PRODUCT_GUIDELINES = [
    ("who-aih", "WHO AIH"),
    ("fda-aiml-saamd-ap", "FDA GMLP/PCCP"),
    ("eu-ai-act", "EU AI Act"),
]
PATIENT_EXPLANATION_COLUMNS = ["C", "K", "B", "D", "F", "E", "I", "H"]
PATIENT_EXPLANATION_GUIDELINES = [
    ("who-aih", "WHO AIH"),
    ("jmsf-ai-medical", "JMSF/JMA"),
    ("eu-ai-act", "EU AI Act"),
]
HOSPITAL_AI_POLICY_COLUMNS = ["A", "B", "H", "I", "L", "M", "D", "C", "F", "G"]
HOSPITAL_AI_POLICY_GUIDELINES = [
    ("nist-ai-rmf", "NIST AI RMF"),
    ("iso-iec-42001", "ISO/IEC 42001"),
    ("jmsf-ai-medical", "JMSF/JMA"),
]
SUPPORTED_TEMPLATES = {
    "samd-consultation-prep": {
        "columns": SAMD_COLUMNS,
        "guidelines": SAMD_GUIDELINES,
        "output_filename": "samd-consultation-prep.md",
        "title_ja": "SaMD事前相談準備シート",
        "audience_ja": "SaMD製造者・申請準備チーム",
        "use_case_ja": "PMDA SaMD 事前相談向けの旧テンプレート。Out of scope のためアーカイブ扱い。",
        "default": False,
        "archived": True,
    },
    "clinical-ai-product-evaluation": {
        "columns": CLINICAL_AI_PRODUCT_COLUMNS,
        "guidelines": CLINICAL_AI_PRODUCT_GUIDELINES,
        "output_filename": "clinical-ai-product-evaluation.md",
        "title_ja": "医療AI製品 導入評価チェックリスト",
        "audience_ja": "臨床医、診療科責任者、院内AI導入審査担当者",
        "use_case_ja": "候補AI製品の適応、リスク、透明性、データ保護、運用責任を導入前に確認する。",
        "default": True,
        "archived": False,
    },
    "patient-explanation-support": {
        "columns": PATIENT_EXPLANATION_COLUMNS,
        "guidelines": PATIENT_EXPLANATION_GUIDELINES,
        "output_filename": "patient-explanation-support.md",
        "title_ja": "患者説明・インフォームドコンセント補助テンプレート",
        "audience_ja": "患者にAI介入を説明する医師、臨床研究者、研究チーム",
        "use_case_ja": "AI利用、利益と限界、代替手段、拒否・撤回、データ利用の説明文を整理する。",
        "default": True,
        "archived": False,
    },
    "hospital-ai-policy-skeleton": {
        "columns": HOSPITAL_AI_POLICY_COLUMNS,
        "guidelines": HOSPITAL_AI_POLICY_GUIDELINES,
        "output_filename": "hospital-ai-policy-skeleton.md",
        "title_ja": "病院AI導入ポリシー骨子",
        "audience_ja": "医療安全部門、情報システム部門、IRB事務局、導入審査会議体",
        "use_case_ja": "院内AI導入時の審査、継続モニタリング、有害事象報告、教育、変更管理を規程化する。",
        "default": True,
        "archived": False,
    },
    "pccp-skeleton": {
        "columns": PCCP_COLUMNS,
        "guidelines": PCCP_GUIDELINES,
        "output_filename": "pccp-skeleton.md",
        "title_ja": "PCCP骨子テンプレート",
        "audience_ja": "臨床研究者、医療機関の導入評価・変更管理担当者",
        "use_case_ja": "AI製品の予定変更、影響評価、検証計画を受け入れ側レビューの観点で確認する。",
        "default": True,
        "archived": False,
    },
    "irb-question-checklist": {
        "columns": IRB_COLUMNS,
        "guidelines": IRB_GUIDELINES,
        "output_filename": "irb-question-checklist.md",
        "title_ja": "医療AI研究 IRB質問票",
        "audience_ja": "臨床研究者、IRB事務局、倫理審査委員",
        "use_case_ja": "透明性、同意、プライバシー、バイアス、人間の監督に関する審査質問を洗い出す。",
        "default": True,
        "archived": False,
    },
}
# Template name -> generated markdown filename. The default generation list excludes
# archived manufacturer-facing templates; archived templates remain available through
# explicit --template selection.
TEMPLATE_OUTPUT_FILENAMES = {
    template_name: spec["output_filename"] for template_name, spec in SUPPORTED_TEMPLATES.items()
}
DEFAULT_TEMPLATES = [
    "clinical-ai-product-evaluation",
    "patient-explanation-support",
    "hospital-ai-policy-skeleton",
    "irb-question-checklist",
    "pccp-skeleton",
]
SECTION_TITLES = {
    "A": "② 該当性判定 (corpus cell A)",
    "B": "③ リスク分類 (corpus cell B)",
    "C": "透明性・説明責任 (corpus cell C)",
    "D": "監査ログ・記録 (corpus cell D)",
    "E": "Human oversight (corpus cell E)",
    "F": "データ品質・バイアス (corpus cell F)",
    "G": "④ PCCP計画 (corpus cell G)",
    "H": "責任主体・説明責任 (corpus cell H)",
    "I": "同意・プライバシー (corpus cell I)",
    "J": "セキュリティ (corpus cell J)",
    "K": "⑤ 臨床評価計画 (corpus cell K)",
    "L": "国際整合・通知導線 (corpus cell L)",
    "M": "⑥ ライフサイクル管理 (corpus cell M)",
}
PCCP_SECTION_SPECS = [
    {
        "title": "① 対象製品/モデルの定義",
        "focus_ja": "PCCPの対象となる製品、モデル、入力、出力、意図する使用、固定境界を明確にする。",
        "prompts": [
            "対象製品、モデルバージョン、構成要素を特定する。",
            "PCCP対象に含める変更と、承認・認証後に別途申請する変更を分ける。",
            "使用者、患者集団、利用環境、モデル出力の臨床的位置づけを記録する。",
        ],
    },
    {
        "title": "② 変更計画 (modification plan)",
        "focus_ja": "予定される変更の種類、変更幅、頻度、発動条件、禁止変更を事前に定義する。",
        "prompts": [
            "性能改善、データ追加、閾値変更、対象集団拡張などの変更類型を列挙する。",
            "各変更の上限、変更しない仕様、臨床ワークフローへの影響を定める。",
            "変更計画が透明性、データ品質、国際整合の観点で説明可能か確認する。",
        ],
    },
    {
        "title": "③ 変更プロトコル (modification protocol)",
        "focus_ja": "変更を実装、検証、承認、リリースする手順と責任者を固定する。",
        "prompts": [
            "変更前レビュー、データ受入基準、モデル更新手順、ロールバック手順を書く。",
            "変更実施時の記録、トレーサビリティ、品質システム上の承認経路を定める。",
            "透明性文書、利用者通知、規制当局向け資料の更新タイミングを設定する。",
        ],
    },
    {
        "title": "④ 影響評価 (impact assessment)",
        "focus_ja": "予定変更が安全性、有効性、データ代表性、バイアス、利用者行動に与える影響を評価する。",
        "prompts": [
            "変更ごとにリスク、便益、想定外使用、患者安全への影響を評価する。",
            "サブグループ性能、データセットシフト、バイアス、透明性への影響を確認する。",
            "国際展開、既存認証、報告義務、インシデント管理への波及を確認する。",
        ],
    },
    {
        "title": "⑤ 検証戦略 (validation strategy)",
        "focus_ja": "変更後モデルが意図する使用に対して十分な性能、安全性、頑健性を保つことを示す。",
        "prompts": [
            "評価データ、主要評価指標、受入基準、サブグループ解析を定義する。",
            "変更前後比較、実世界性能監視、失敗時の停止基準を定める。",
            "検証結果を利用者、規制当局、監査者が追跡できる形にする。",
        ],
    },
    {
        "title": "⑥ 報告/通知計画",
        "focus_ja": "変更、性能低下、重大インシデント、利用者向け更新情報の報告経路を決める。",
        "prompts": [
            "利用者、医療機関、規制当局、社内責任者への通知条件を定義する。",
            "重大インシデント、性能逸脱、回収・停止判断のエスカレーションを定める。",
            "海外制度や整合規格への影響を確認し、必要な文書更新を記録する。",
        ],
    },
]
IRB_SECTION_SPECS = [
    {
        "title": "② 該当性 (cell A)",
        "focus_ja": "研究が医療AI、医療機器、生成AI、臨床利用、二次利用のどれに該当するかを確認する。",
        "columns": ["A"],
        "questions": [
            "研究対象AIの用途は診療、研究支援、患者向け説明、事務支援のどれか。",
            "AI出力は医師または研究者の判断を代替、補助、生成するか。",
            "既存研究、品質改善、医療機器評価、臨床研究の境界は明確か。",
        ],
    },
    {
        "title": "③ リスク評価 (cell B)",
        "focus_ja": "患者、研究参加者、医療者、研究組織に生じるリスクと便益を文脈別に確認する。",
        "columns": ["B"],
        "questions": [
            "誤出力、過信、自動化バイアス、診療遅延、心理的影響を評価したか。",
            "高リスク集団や脆弱な参加者に固有のリスクを分けているか。",
            "残余リスクを誰が受容し、どの条件で研究を停止するか。",
        ],
    },
    {
        "title": "④ 透明性/説明責任 (cell C, F)",
        "focus_ja": "AI使用の説明、出力根拠、限界、データ品質、説明責任の所在を確認する。",
        "columns": ["C", "F"],
        "questions": [
            "参加者、患者、医療者にAI利用の事実と限界をどう説明するか。",
            "モデルの入力、出力、性能、既知の限界、データ代表性を文書化したか。",
            "説明不能な出力や不一致が出た場合の責任者と対応手順は明確か。",
        ],
    },
    {
        "title": "⑤ バイアス/公平性 (cell D, 補助参照 cell F)",
        "focus_ja": "記録・監査可能性とデータ品質の両面から、偏りの発見、説明、是正可能性を確認する。",
        "columns": ["D", "F"],
        "questions": [
            "年齢、性別、疾患、施設、言語、社会経済属性ごとの性能差を確認したか。",
            "バイアスを発見した場合の記録、原因分析、是正、再審査手順はあるか。",
            "研究対象集団が学習・評価データと異なる場合の説明は十分か。",
        ],
    },
    {
        "title": "⑥ プライバシー/データ保護 (cell H, 補助参照 cell I)",
        "focus_ja": "責任主体、データ管理責任、同意・機密性・個人情報保護の実装を確認する。",
        "columns": ["H", "I"],
        "questions": [
            "データ管理者、解析者、モデル提供者、研究責任者の責任分担は明確か。",
            "個人情報、要配慮情報、診療情報、二次利用データの取扱いは法令・倫理指針に沿うか。",
            "外部モデル、クラウド、委託先にデータが渡る場合の契約と保護措置はあるか。",
        ],
    },
    {
        "title": "⑦ インフォームドコンセント (cell I)",
        "focus_ja": "参加者に対してAI利用、データ利用、リスク、撤回、二次利用を理解可能に説明する。",
        "columns": ["I"],
        "questions": [
            "説明文書はAIの役割、限界、データ利用範囲、第三者提供を明示しているか。",
            "同意免除またはオプトアウトの場合、理由と代替保護措置は妥当か。",
            "同意撤回後のデータ、学習済みモデル、派生データの扱いを説明しているか。",
        ],
    },
    {
        "title": "⑧ モニタリング/有害事象 (cell L)",
        "focus_ja": "研究中および研究後の監視、逸脱、インシデント、有害事象、外部報告の導線を確認する。",
        "columns": ["L"],
        "questions": [
            "AI出力による有害事象、ニアミス、予期せぬ性能低下をどう検知するか。",
            "IRB、研究機関、規制当局、共同研究先への報告基準と期限は明確か。",
            "海外ガイダンスや国際倫理との整合を継続的に見直す仕組みはあるか。",
        ],
    },
]


CLINICAL_AI_PRODUCT_SECTION_SPECS = [
    {
        "title": "① 製品概要",
        "focus_ja": "導入候補AIの用途、臨床的位置づけ、利用環境、利用者、患者集団を整理する。",
        "columns": ["A"],
        "prompts": [
            "AIが支援する診療行為、対象患者、利用場面、除外条件を記載する。",
            "AI出力が診断、治療方針、トリアージ、文書作成、患者説明のどこに影響するかを分ける。",
            "医師、看護師、患者、ベンダー、院内管理者の関与範囲を記録する。",
        ],
    },
    {
        "title": "② 適応 (cell A)",
        "focus_ja": "候補製品の適用対象と、自施設での実使用条件が一致するかを確認する。",
        "columns": ["A"],
        "prompts": [
            "添付文書、利用規約、説明資料に書かれた intended use と現場の使い方は一致するか。",
            "対象疾患、年齢層、検査種別、診療科、施設規模に外挿がないか。",
            "研究利用、診療補助、患者向け利用、管理業務利用の境界は明確か。",
        ],
    },
    {
        "title": "③ リスク評価 (cell B)",
        "focus_ja": "誤出力、過信、診療遅延、責任分担などのリスクを臨床文脈で整理する。",
        "columns": ["B"],
        "prompts": [
            "AIの誤判定が患者安全に与える最大影響を具体的に書く。",
            "人間の確認で検出できるリスクと、検出しにくいリスクを分ける。",
            "高リスク患者、緊急時、夜間休日、経験の浅い利用者でリスクが変わるか確認する。",
        ],
    },
    {
        "title": "④ 透明性/説明可能性 (cell C, F)",
        "focus_ja": "利用者と患者が、AIの役割、性能、限界、データ根拠を理解できるかを確認する。",
        "columns": ["C", "F"],
        "prompts": [
            "医師がAI出力の意味、根拠、信頼区間、適用外条件を説明できるか。",
            "学習・評価データの代表性、外部検証、性能指標、更新日が入手できるか。",
            "説明できない出力を診療に使わない条件、または追加確認の条件を定める。",
        ],
    },
    {
        "title": "⑤ バイアス/限界 (cell D)",
        "focus_ja": "性能差、監査可能性、記録、想定外使用を確認し、限界を運用ルールに落とす。",
        "columns": ["D", "F"],
        "prompts": [
            "年齢、性別、疾患、施設、言語、検査機器、データ欠損による性能差を確認したか。",
            "AI利用履歴、出力、医師判断、最終判断の記録を後から追跡できるか。",
            "限界が見つかったときに、利用停止、対象制限、患者説明更新へつなげる手順はあるか。",
        ],
    },
    {
        "title": "⑥ データ保護 (cell H)",
        "focus_ja": "患者データの責任主体、外部提供、保存、再利用、委託先管理を確認する。",
        "columns": ["H", "I", "J"],
        "prompts": [
            "データ管理責任者、処理者、委託先、ベンダーの責任分担は契約上明確か。",
            "診療情報がクラウド、外部API、モデル改善、二次利用に使われるか確認したか。",
            "アクセス制御、ログ、匿名化・仮名化、患者説明、問い合わせ窓口を確認したか。",
        ],
    },
    {
        "title": "⑦ 運用・監査・責任 (cell L, 責任所在)",
        "focus_ja": "導入後監視、監査、エスカレーション、国際基準との整合、責任所在を固定する。",
        "columns": ["L", "H", "M"],
        "prompts": [
            "AI出力の採否、患者説明、有害事象対応の最終責任者を定める。",
            "性能低下、インシデント、苦情、想定外使用をどの会議体へ報告するか決める。",
            "導入後レビューの頻度、監査項目、停止基準、ベンダー再評価条件を記録する。",
        ],
    },
]

PATIENT_EXPLANATION_SECTION_SPECS = [
    {
        "title": "① AIを使用する旨の説明",
        "focus_ja": "診療または研究でAIがどの役割を担うか、患者に理解できる言葉で説明する。",
        "columns": ["C"],
        "prompts": [
            "この診療・検査・説明でAIを使うことを明示する。",
            "AIは医師の判断を補助するもので、最終判断者を明確にする。",
            "患者が質問できる窓口と、AIを使う範囲を伝える。",
        ],
    },
    {
        "title": "② 想定利益",
        "focus_ja": "AI利用により期待される診療上・説明上の利益を、過大に約束せず整理する。",
        "columns": ["K", "C"],
        "prompts": [
            "診断補助、見落とし低減、待ち時間短縮、説明の標準化など期待される利益を書く。",
            "利益は保証ではなく、個々の患者で結果が異なることを説明する。",
            "医師がAI出力を確認し、必要に応じて追加検査や通常診療を行うことを明記する。",
        ],
    },
    {
        "title": "③ 既知の限界・リスク (cell B, D)",
        "focus_ja": "誤出力、偏り、説明不能性、過信、記録・監査上の限界を患者説明に落とす。",
        "columns": ["B", "D", "F"],
        "prompts": [
            "AIが誤った提案、過不足のある説明、患者背景に合わない出力を出す可能性を伝える。",
            "年齢、疾患、検査条件、データの偏りにより性能が変わる可能性を説明する。",
            "AI利用の記録、問題発生時の確認手順、医師による再確認を伝える。",
        ],
    },
    {
        "title": "④ 代替手段",
        "focus_ja": "AIを使わない通常診療、医師判断、追加検査、セカンドオピニオンを選べることを説明する。",
        "columns": ["E", "C"],
        "prompts": [
            "AIを使わない場合の診療手順や説明方法を伝える。",
            "AIの提案と医師判断が異なる場合の扱いを説明する。",
            "必要に応じて追加検査、専門医相談、セカンドオピニオンが可能であることを伝える。",
        ],
    },
    {
        "title": "⑤ 拒否/撤回の権利 (cell I)",
        "focus_ja": "AI利用、データ利用、二次利用への同意・拒否・撤回を説明する。",
        "columns": ["I", "H"],
        "prompts": [
            "AI利用やデータ利用を拒否できる範囲、拒否時の診療への影響を説明する。",
            "撤回後のデータ、記録、既に実施された解析結果の扱いを明示する。",
            "外部サービス、クラウド、ベンダー改善利用がある場合は別に説明する。",
        ],
    },
]

HOSPITAL_AI_POLICY_SECTION_SPECS = [
    {
        "title": "① 適用範囲",
        "focus_ja": "院内で審査対象とするAI利用を、診療、研究、教育、事務、患者向け利用に分ける。",
        "columns": ["A"],
        "prompts": [
            "診療判断に影響するAI、文書作成AI、患者向けAI、研究AI、業務支援AIを分類する。",
            "院内承認が必要な利用、部門判断で足りる利用、禁止する利用を定める。",
            "外部クラウド、生成AI、医療機器、研究用ツールの扱いを分ける。",
        ],
    },
    {
        "title": "② 導入審査プロセス (cell A, B)",
        "focus_ja": "導入前に、適用対象、リスク、責任、データ保護、患者説明を審査する流れを定める。",
        "columns": ["A", "B", "H", "I"],
        "prompts": [
            "申請者、審査会議体、必要資料、承認条件、再審査条件を定める。",
            "患者安全、個人情報、医師の監督、ベンダー契約、研究該当性を確認する。",
            "高リスク利用は医療安全、情報システム、倫理、法務、診療部門で共同審査する。",
        ],
    },
    {
        "title": "③ 継続モニタリング (cell L)",
        "focus_ja": "導入後の性能、利用状況、苦情、インシデント、国際基準との整合を継続確認する。",
        "columns": ["L", "M", "D"],
        "prompts": [
            "監視指標、レビュー頻度、責任部署、報告先を定める。",
            "性能低下、対象外利用、患者影響、ベンダー更新を検知する手順を書く。",
            "国際基準や専門職答申の更新時に院内ルールを見直す。",
        ],
    },
    {
        "title": "④ 有害事象報告",
        "focus_ja": "AI利用に関連する有害事象、ニアミス、説明誤り、情報漏えいの報告経路を定める。",
        "columns": ["D", "B", "H"],
        "prompts": [
            "報告対象、期限、一次対応、患者説明、ベンダー連絡、再発防止を定義する。",
            "AI出力、医師判断、最終対応、ログ、証跡を保存する。",
            "医療安全報告、情報セキュリティ報告、倫理審査報告の分岐を決める。",
        ],
    },
    {
        "title": "⑤ 教育・トレーニング (cell M)",
        "focus_ja": "利用者がAIの限界、過信リスク、説明責任、データ保護を理解する教育を定める。",
        "columns": ["M", "C", "F", "I"],
        "prompts": [
            "初回利用前、定期更新時、重大変更時に必要な教育内容を定める。",
            "AI出力の確認方法、患者説明、拒否対応、インシデント報告を訓練する。",
            "職種別に医師、看護師、事務、研究者、情報システム担当の教育範囲を分ける。",
        ],
    },
    {
        "title": "⑥ 変更管理 (cell G)",
        "focus_ja": "モデル更新、閾値変更、対象拡大、ベンダー仕様変更を院内で再評価する。",
        "columns": ["G", "M", "D"],
        "prompts": [
            "変更通知を受ける窓口、影響評価、再承認、利用者通知、患者説明更新を定める。",
            "性能、対象患者、利用環境、データ処理が変わる場合の停止・再開基準を書く。",
            "変更履歴、承認履歴、検証結果、教育実施を監査可能に保存する。",
        ],
    },
]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value).strip()
    return html.escape(text).replace("\n", "<br>").replace("|", "\\|")


def load_columns(required_columns: list[str]) -> dict[str, dict[str, Any]]:
    doc = load_yaml(COLUMNS_PATH) or {}
    columns = doc.get("columns", [])
    if not isinstance(columns, list):
        raise ValueError(f"{COLUMNS_PATH}: columns must be a list")
    by_id = {column["id"]: column for column in columns}
    missing = [column for column in required_columns if column not in by_id]
    if missing:
        raise ValueError(f"{COLUMNS_PATH}: missing target columns {missing}")
    return by_id


def load_guidelines() -> dict[str, dict[str, Any]]:
    guidelines: dict[str, dict[str, Any]] = {}
    for path in sorted(GUIDELINES_DIR.glob("*.yml")):
        doc = load_yaml(path)
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: guideline YAML must be a mapping")
        guideline_id = doc.get("id")
        if not isinstance(guideline_id, str):
            raise ValueError(f"{path}: guideline id is required")
        cells = doc.get("cells", [])
        if not isinstance(cells, list):
            raise ValueError(f"{path}: cells must be a list")
        doc["_cells_by_column"] = {cell["column"]: cell for cell in cells}
        guidelines[guideline_id] = doc
    return guidelines


def build_column_context(
    column_id: str,
    columns_by_id: dict[str, dict[str, Any]],
    guidelines_by_id: dict[str, dict[str, Any]],
    target_guidelines: list[tuple[str, str]],
    section_title: str | None = None,
) -> dict[str, Any]:
    column = dict(columns_by_id[column_id])
    column["column"] = column_id
    column["section_title"] = section_title or SECTION_TITLES[column_id]
    items = []
    for guideline_id, short_name in target_guidelines:
        guideline = guidelines_by_id[guideline_id]
        cell = guideline["_cells_by_column"].get(column_id)
        if cell is None:
            raise ValueError(f"{guideline_id}: missing cell {column_id}")
        citation = cell.get("citation") or {}
        if not citation.get("url"):
            raise ValueError(f"{guideline_id} cell {column_id}: citation.url is required")
        items.append(
            {
                "guideline_id": guideline_id,
                "short_name": short_name,
                "guideline_name_ja": guideline.get("name_ja", guideline_id),
                "guideline_url": guideline.get("url", ""),
                "requirement": cell.get("requirement", ""),
                "summary_ja": cell.get("summary_ja", ""),
                "citation": {
                    "url": citation.get("url", ""),
                    "section": citation.get("section", "source"),
                    "confidence": citation.get("confidence", "unknown"),
                },
            }
        )
    column["items"] = items
    return column


def hydrate_section_specs(
    specs: list[dict[str, Any]],
    columns_by_id: dict[str, dict[str, Any]],
    guidelines_by_id: dict[str, dict[str, Any]],
    target_guidelines: list[tuple[str, str]],
    target_columns: list[str],
) -> list[dict[str, Any]]:
    return [
        {
            **section,
            "columns": [
                build_column_context(
                    column_id,
                    columns_by_id,
                    guidelines_by_id,
                    target_guidelines,
                    SECTION_TITLES[column_id],
                )
                for column_id in section.get("columns", target_columns)
            ],
        }
        for section in specs
    ]


def build_context(template_name: str) -> dict[str, Any]:
    spec = SUPPORTED_TEMPLATES[template_name]
    target_columns = spec["columns"]
    target_guidelines = spec["guidelines"]
    columns_by_id = load_columns(target_columns)
    guidelines_by_id = load_guidelines()
    missing_guidelines = [
        guideline_id
        for guideline_id, _short_name in target_guidelines
        if guideline_id not in guidelines_by_id
    ]
    if missing_guidelines:
        raise ValueError(f"missing target guidelines {missing_guidelines}")

    sections = [
        build_column_context(
            column_id,
            columns_by_id,
            guidelines_by_id,
            target_guidelines,
            SECTION_TITLES[column_id],
        )
        for column_id in target_columns
    ]

    pccp_sections = []
    if template_name == "pccp-skeleton":
        pccp_sections = hydrate_section_specs(
            PCCP_SECTION_SPECS,
            columns_by_id,
            guidelines_by_id,
            target_guidelines,
            target_columns,
        )

    irb_sections = []
    if template_name == "irb-question-checklist":
        irb_sections = hydrate_section_specs(
            IRB_SECTION_SPECS,
            columns_by_id,
            guidelines_by_id,
            target_guidelines,
            target_columns,
        )

    clinical_ai_product_sections = []
    if template_name == "clinical-ai-product-evaluation":
        clinical_ai_product_sections = hydrate_section_specs(
            CLINICAL_AI_PRODUCT_SECTION_SPECS,
            columns_by_id,
            guidelines_by_id,
            target_guidelines,
            target_columns,
        )

    patient_explanation_sections = []
    if template_name == "patient-explanation-support":
        patient_explanation_sections = hydrate_section_specs(
            PATIENT_EXPLANATION_SECTION_SPECS,
            columns_by_id,
            guidelines_by_id,
            target_guidelines,
            target_columns,
        )

    hospital_ai_policy_sections = []
    if template_name == "hospital-ai-policy-skeleton":
        hospital_ai_policy_sections = hydrate_section_specs(
            HOSPITAL_AI_POLICY_SECTION_SPECS,
            columns_by_id,
            guidelines_by_id,
            target_guidelines,
            target_columns,
        )

    source_guidelines = []
    for guideline_id, short_name in target_guidelines:
        guideline = guidelines_by_id[guideline_id]
        source_guidelines.append(
            {
                "id": guideline_id,
                "short_name": short_name,
                "name_ja": guideline.get("name_ja", guideline_id),
                "summary_ja": guideline.get("summary_ja", ""),
                "url": guideline.get("url", ""),
            }
        )

    return {
        "template_name": template_name,
        "sections": sections,
        "pccp_sections": pccp_sections,
        "irb_sections": irb_sections,
        "clinical_ai_product_sections": clinical_ai_product_sections,
        "patient_explanation_sections": patient_explanation_sections,
        "hospital_ai_policy_sections": hospital_ai_policy_sections,
        "source_guidelines": source_guidelines,
        "target_columns": target_columns,
        "target_guidelines": target_guidelines,
    }


def render_evidence_pack(template_name: str) -> Path:
    if template_name not in SUPPORTED_TEMPLATES:
        supported = ", ".join(sorted(SUPPORTED_TEMPLATES))
        raise ValueError(f"unsupported template: {template_name}. supported: {supported}")

    template_path = TEMPLATES_DIR / f"{template_name}.md.j2"
    if not template_path.exists():
        template_path = TEMPLATES_DIR / "_archived" / f"{template_name}.md.j2"
    if not template_path.exists():
        raise FileNotFoundError(template_path)

    env = Environment(
        loader=None,
        undefined=StrictUndefined,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["md"] = md_escape
    template = env.from_string(template_path.read_text(encoding="utf-8"))
    content = template.render(**build_context(template_name)).rstrip() + "\n"

    BUILD_EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    output_path = BUILD_EVIDENCE_DIR / TEMPLATE_OUTPUT_FILENAMES[template_name]
    output_path.write_text(content, encoding="utf-8")
    return output_path


def generate_all_evidence_packs() -> list[Path]:
    clean_default_evidence_outputs()
    return [render_evidence_pack(template_name) for template_name in DEFAULT_TEMPLATES]


def clean_default_evidence_outputs() -> None:
    if not BUILD_EVIDENCE_DIR.exists():
        return
    target_filenames = {TEMPLATE_OUTPUT_FILENAMES[template_name] for template_name in DEFAULT_TEMPLATES}
    for stale in BUILD_EVIDENCE_DIR.glob("*.md"):
        if stale.name not in target_filenames:
            stale.unlink()


def copy_evidence_to_site_public(template_names: list[str] | None = None) -> None:
    if not BUILD_EVIDENCE_DIR.exists():
        return
    target_names = template_names or DEFAULT_TEMPLATES
    SITE_PUBLIC_EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    target_filenames = {TEMPLATE_OUTPUT_FILENAMES[template_name] for template_name in target_names}
    for stale in SITE_PUBLIC_EVIDENCE_DIR.glob("*.md"):
        if stale.name not in target_filenames:
            stale.unlink()
    for template_name in target_names:
        source = BUILD_EVIDENCE_DIR / TEMPLATE_OUTPUT_FILENAMES[template_name]
        if source.exists():
            shutil.copy2(source, SITE_PUBLIC_EVIDENCE_DIR / source.name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate static evidence pack markdown files.")
    parser.add_argument(
        "--template",
        choices=sorted(SUPPORTED_TEMPLATES),
        help="Evidence pack template name. Omit to generate the default clinical/research/hospital packs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.template:
        output_path = render_evidence_pack(args.template)
        print(f"generated: {output_path.relative_to(ROOT)}")
        return 0

    output_paths = generate_all_evidence_packs()
    for output_path in output_paths:
        print(f"generated: {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
