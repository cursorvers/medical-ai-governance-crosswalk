export type RequirementLevel = "must" | "should" | "mention" | "none" | "not_assessed" | "source_unavailable";
export type ConfidenceLevel = "high" | "medium" | "low";
export interface Citation {
    url: string;
    section?: string;
    retrieved?: string;
    confidence?: ConfidenceLevel;
}
export interface Cell {
    column: string;
    requirement: RequirementLevel;
    summary_ja: string;
    citation: Citation;
    notes_ja?: string;
}
export interface SourceDocument {
    url: string;
    note_ja?: string;
    note_en?: string;
}
export interface Guideline {
    id: string;
    name_ja: string;
    name_en: string;
    issuer: string;
    jurisdiction: string;
    type: string;
    url: string;
    version?: string;
    published_date?: string;
    last_reviewed?: string;
    source_hash?: string;
    maintainer?: string;
    tags?: string[];
    source_documents?: SourceDocument[];
    summary_ja?: string;
    cells: Cell[];
}
export interface Corpus {
    schema_version: string;
    generated_at: string;
    source: string;
    guideline_count: number;
    guidelines: Guideline[];
}
export declare const guidelines: Guideline[];
export declare const corpusMetadata: {
    schema_version: string;
    generated_at: string;
    source: string;
    guideline_count: number;
};
export default guidelines;
