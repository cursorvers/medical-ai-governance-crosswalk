"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.corpusMetadata = exports.guidelines = void 0;
const corpus_json_1 = __importDefault(require("./corpus.json"));
const typedCorpus = corpus_json_1.default;
exports.guidelines = typedCorpus.guidelines;
exports.corpusMetadata = {
    schema_version: typedCorpus.schema_version,
    generated_at: typedCorpus.generated_at,
    source: typedCorpus.source,
    guideline_count: typedCorpus.guideline_count
};
exports.default = exports.guidelines;
