---
title: Home
---

<div class="gl-landing">
  <section class="gl-lp-hero" aria-labelledby="gl-hero-title">
    <div class="gl-hero-bg-mark" aria-hidden="true"></div>
    <div class="gl-lp-inner gl-hero-grid">
      <div class="gl-hero-copy">
        <p class="gl-eyebrow">医療AI 公開ガイドライン 10本×13論点</p>
        <h1 id="gl-hero-title">「このAI、うちで使って大丈夫？」<br>そう迷ったら、公開ガイドラインで確かめる。</h1>
        <p class="gl-hero-subcopy">医療AI公開ガイドライン10本の本文URLを13論点で横断検索。<br>LLMの生成回答ではなく、一次資料への導線だけを返します。</p>
      </div>

      <div class="gl-hero-search" aria-label="ガイドライン検索">
        <p class="gl-search-label">患者説明・院内検討・研究申請の論点を引く</p>
        <div id="gl-lookup">
          <input type="text" id="gl-query" placeholder="例: うちで使って大丈夫？ 承認は取れている？" aria-label="医療AIガイドライン論点検索">
          <div class="gl-suggest" aria-label="検索候補">
            <button class="gl-suggest-btn" type="button" data-query="安全性">うちで使って問題ない？</button>
            <button class="gl-suggest-btn" type="button" data-query="責任主体">承認は取れている？</button>
            <button class="gl-suggest-btn" type="button" data-query="説明責任">判断根拠は示せる？</button>
            <button class="gl-suggest-btn" type="button" data-query="バイアス">患者背景に偏りは？</button>
          </div>
          <div id="gl-results"></div>
        </div>
      </div>
    </div>
    <a class="gl-scroll-hint" href="#clinical-now">外来で今すぐ引く</a>
  </section>

  <aside class="gl-disclaimer-strip" role="note">
    <p>⚠️ 本サイトは公開ガイドラインの参照用コンパイルです。法的助言・規制適合性の保証・診療判断ではありません。ご利用前に必ず原文を参照してください。</p>
  </aside>

  <section class="gl-section gl-primary" id="clinical-now" aria-labelledby="clinical-now-title">
    <div class="gl-lp-inner">
      <div class="gl-section-heading">
        <span class="gl-icon gl-icon-stethoscope" aria-hidden="true"></span>
        <div>
          <p class="gl-kicker">臨床医向け</p>
          <h2 id="clinical-now-title">導入の前に、自分で確かめる</h2>
        </div>
      </div>
      <div class="gl-usecase-grid">
        <button class="gl-usecase-card gl-suggest-btn" type="button" data-query="安全性">
          <span>導入を検討するとき</span>
          <strong>このAI、自分の臨床で使って大丈夫？</strong>
          <small>安全性・臨床評価・Human oversight を横断します。</small>
        </button>
        <button class="gl-usecase-card gl-suggest-btn" type="button" data-query="説明責任">
          <span>判断根拠に迷ったら</span>
          <strong>なぜその結果になったか、説明できる？</strong>
          <small>説明責任・透明性・責任主体を確認します。</small>
        </button>
        <button class="gl-usecase-card gl-suggest-btn" type="button" data-query="バイアス">
          <span>適用範囲が気になったら</span>
          <strong>うちの患者層でも性能は保たれる？</strong>
          <small>データ品質・バイアス・同意プライバシーを探します。</small>
        </button>
      </div>
    </div>
  </section>

  <section class="gl-section gl-secondary" aria-labelledby="hospital-title">
    <div class="gl-lp-inner gl-split">
      <div class="gl-section-heading">
        <span class="gl-icon gl-icon-hospital" aria-hidden="true"></span>
        <div>
          <p class="gl-kicker">病院AI導入委員会向け</p>
          <h2 id="hospital-title">病院でAI導入を検討している方へ</h2>
        </div>
      </div>
      <div class="gl-action-panel">
        <p>院内でAIを使う前に、責任主体、監査ログ、説明、セキュリティ、臨床評価の論点をそろえます。</p>
        <a class="gl-cta" href="evidence/hospital-ai-policy-skeleton.md">病院AI導入ポリシー骨子 DL</a>
      </div>
    </div>
  </section>

  <section class="gl-section gl-tertiary" aria-labelledby="irb-title">
    <div class="gl-lp-inner gl-split">
      <div class="gl-section-heading">
        <span class="gl-icon gl-icon-irb" aria-hidden="true"></span>
        <div>
          <p class="gl-kicker">IRB事務局・臨床研究者向け</p>
          <h2 id="irb-title">AI使った臨床研究を始める方へ</h2>
        </div>
      </div>
      <div class="gl-action-panel">
        <p>申請前に、同意、プライバシー、データ品質、バイアス、Human oversight の質問漏れを減らします。</p>
        <a class="gl-cta gl-cta-secondary" href="evidence/irb-question-checklist.md">IRB質問チェックリスト DL</a>
      </div>
    </div>
  </section>

  <section class="gl-section gl-trust" aria-labelledby="trust-title">
    <div class="gl-lp-inner">
      <div class="gl-trust-meta">
        <div>
          <p class="gl-kicker">Trust Bar</p>
          <h2 id="trust-title">収録GL 10本</h2>
        </div>
        <p class="gl-last-updated">最終更新日: {{last_updated}}</p>
      </div>
      <ol class="gl-guideline-list">
        <li>PMDA SaMD情報ページ</li>
        <li>MHLW 医療機器プログラム取扱い</li>
        <li>FDA AI/ML SaMD アクションプラン + PCCPガイダンス</li>
        <li>EU AI法</li>
        <li>IMDRF SaMD作業部会</li>
        <li>ISO/IEC 42001</li>
        <li>NIST AI RMF</li>
        <li>WHO AI for Health</li>
        <li>日本医師会 AI臨床利用答申</li>
        <li>経済産業省 AI事業者ガイドライン</li>
      </ol>
      <p class="gl-disclaimer">本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。SaMD製造者の承認申請支援は対象外です。利用前に必ず原文を参照してください。</p>
    </div>
  </section>

  <section class="gl-section gl-supervision" aria-labelledby="supervision-title">
    <div class="gl-lp-inner gl-supervision-grid">
      <div>
        <p class="gl-kicker">医学的監修</p>
        <h2 id="supervision-title">独立編集委員会によるピアレビューを継続募集中</h2>
        <p>現時点で未監修ですが、すべての要約に原文URLを併記し、変更履歴・GitHub差分を公開しています。医学的判断ではなく、一次資料への導線としてご活用ください。</p>
        <ul class="gl-trust-signal">
          <li>📚 根拠パック: 公開GL 10本 / 引用URL直リンク / LLM生成回答なし</li>
          <li>📝 最終更新日: {{last_updated}}</li>
          <li>👥 <a href="https://github.com/cursorvers/medical-ai-governance-crosswalk/graphs/contributors">GitHub contributors</a></li>
          <li>💡 修正提案: <a href="https://github.com/cursorvers/medical-ai-governance-crosswalk/issues">GitHub Issue</a> で歓迎</li>
        </ul>
      </div>
      <div>
        <p class="gl-kicker">更新履歴 (直近5件)</p>
        <div class="gl-changelog">
{{changelog_recent5}}
        </div>
      </div>
    </div>
  </section>

  <section class="gl-section gl-evidence-pack" aria-labelledby="evidence-pack-title">
    <div class="gl-lp-inner">
      <p class="gl-kicker">📦 Evidence Pack</p>
      <h2 id="evidence-pack-title">根拠パック — 一次資料への導線</h2>
      <p>このサイトは LLM の生成回答ではなく、公開ガイドライン一次資料への導線です。以下は Markdown テンプレート、CC-BY 4.0 で改変・再配布可能。</p>
      <ul class="gl-evidence-list">
        <li><a href="evidence/clinical-ai-product-evaluation.md">臨床AI製品導入評価チェックリスト</a></li>
        <li><a href="evidence/patient-explanation-support.md">患者説明サポート資料</a></li>
        <li><a href="evidence/hospital-ai-policy-skeleton.md">病院AI導入ポリシー骨子</a></li>
        <li><a href="evidence/irb-question-checklist.md">IRB質問チェックリスト</a></li>
        <li><a href="evidence/pccp-skeleton.md">PCCP骨子</a></li>
      </ul>
    </div>
  </section>

  <footer class="gl-lp-footer">
    <div class="gl-lp-inner">
      <p>License: CC-BY 4.0 + MIT</p>
      <p><a href="https://github.com/cursorvers/medical-ai-governance-crosswalk">GitHub</a> / <a href="https://github.com/cursorvers/medical-ai-governance-crosswalk/issues">Issue</a></p>
    </div>
  </footer>
</div>

<script src="assets/lookup.js"></script>
