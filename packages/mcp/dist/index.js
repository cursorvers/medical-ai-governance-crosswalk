#!/usr/bin/env node
"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const index_js_1 = require("@modelcontextprotocol/sdk/server/index.js");
const stdio_js_1 = require("@modelcontextprotocol/sdk/server/stdio.js");
const types_js_1 = require("@modelcontextprotocol/sdk/types.js");
const lookup_index_json_1 = __importDefault(require("./lookup-index.json"));
const typedCorpus = lookup_index_json_1.default;
function search(query) {
    const qLower = query.toLowerCase();
    const matchedColumnIds = new Set();
    const columnLevelMatches = new Set();
    const cellLevelMatches = new Map();
    const exactKeywordMatches = typedCorpus.keywords[query];
    if (exactKeywordMatches) {
        for (const columnId of exactKeywordMatches) {
            matchedColumnIds.add(columnId);
            columnLevelMatches.add(columnId);
        }
    }
    for (const [keyword, columnIds] of Object.entries(typedCorpus.keywords)) {
        if (keyword.toLowerCase().includes(qLower)) {
            for (const columnId of columnIds) {
                matchedColumnIds.add(columnId);
                columnLevelMatches.add(columnId);
            }
        }
    }
    for (const [columnId, column] of Object.entries(typedCorpus.columns)) {
        if (column.name.toLowerCase().includes(qLower) || column.name_en.toLowerCase().includes(qLower)) {
            matchedColumnIds.add(columnId);
            columnLevelMatches.add(columnId);
        }
        for (const cell of column.cells) {
            if (cell.summary.toLowerCase().includes(qLower) || cell.guideline.toLowerCase().includes(qLower)) {
                matchedColumnIds.add(columnId);
                const cells = cellLevelMatches.get(columnId) ?? [];
                cells.push(cell);
                cellLevelMatches.set(columnId, cells);
            }
        }
    }
    return [...matchedColumnIds].sort().map((columnId) => {
        const column = typedCorpus.columns[columnId];
        const cellMatches = cellLevelMatches.get(columnId);
        return {
            column_id: columnId,
            column_name: column.name,
            column_name_en: column.name_en,
            cells: columnLevelMatches.has(columnId) || !cellMatches ? column.cells : cellMatches,
        };
    });
}
function listColumns() {
    return Object.entries(typedCorpus.columns)
        .map(([id, column]) => ({
        id,
        name: column.name,
        name_en: column.name_en,
        cell_count: column.cells.length,
    }))
        .sort((a, b) => a.id.localeCompare(b.id));
}
function listGuidelines() {
    const guidelines = new Map();
    for (const column of Object.values(typedCorpus.columns)) {
        for (const cell of column.cells) {
            if (!guidelines.has(cell.guideline_id)) {
                guidelines.set(cell.guideline_id, cell.guideline);
            }
        }
    }
    return [...guidelines.entries()]
        .map(([guideline_id, guideline]) => ({ guideline_id, guideline }))
        .sort((a, b) => a.guideline_id.localeCompare(b.guideline_id));
}
function getStringArg(args, name) {
    const value = args[name];
    if (typeof value !== "string") {
        throw new Error(`Missing string argument: ${name}`);
    }
    return value;
}
function asTextContent(result) {
    return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
    };
}
const server = new index_js_1.Server({
    name: "medgov",
    version: "0.1.0",
}, {
    capabilities: {
        tools: {},
    },
});
server.setRequestHandler(types_js_1.ListToolsRequestSchema, async () => ({
    tools: [
        {
            name: "search_medical_governance",
            description: "Search the medical AI governance crosswalk (PMDA/FDA/EU AI Act/WHO/IMDRF/ISO-IEC 42001/NIST AI RMF/MHLW/METI/JMA). Returns matching columns and cells with citations and strength labels.",
            inputSchema: {
                type: "object",
                properties: {
                    query: { type: "string", description: "keyword, Japanese or English" },
                },
                required: ["query"],
            },
        },
        {
            name: "get_column",
            description: "Return full detail (all 10 cells) for one column A-M.",
            inputSchema: {
                type: "object",
                properties: {
                    column_id: { type: "string", enum: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"] },
                },
                required: ["column_id"],
            },
        },
        {
            name: "get_guideline",
            description: "Return all 13 cells belonging to one guideline (one per column). Use list_guidelines to discover IDs.",
            inputSchema: {
                type: "object",
                properties: {
                    guideline_id: { type: "string" },
                },
                required: ["guideline_id"],
            },
        },
        {
            name: "list_guidelines",
            description: "List the 10 guidelines (guideline_id + display name).",
            inputSchema: { type: "object", properties: {} },
        },
        {
            name: "list_columns",
            description: "List the 13 columns (id, name, name_en, cell_count).",
            inputSchema: { type: "object", properties: {} },
        },
    ],
}));
server.setRequestHandler(types_js_1.CallToolRequestSchema, async (request) => {
    const name = request.params.name;
    const args = (request.params.arguments ?? {});
    switch (name) {
        case "search_medical_governance": {
            const query = getStringArg(args, "query");
            const matches = search(query);
            return asTextContent({ query, match_count: matches.length, matches });
        }
        case "get_column": {
            const columnId = getStringArg(args, "column_id");
            const column = typedCorpus.columns[columnId];
            if (!column) {
                throw new Error(`Column not found: ${columnId}`);
            }
            return asTextContent({
                column_id: columnId,
                name: column.name,
                name_en: column.name_en,
                cells: column.cells,
            });
        }
        case "get_guideline": {
            const guidelineId = getStringArg(args, "guideline_id");
            const cells = Object.entries(typedCorpus.columns)
                .flatMap(([columnId, column]) => column.cells
                .filter((cell) => cell.guideline_id === guidelineId)
                .map((cell) => ({
                column_id: columnId,
                column_name: column.name,
                column_name_en: column.name_en,
                strength: cell.strength,
                summary: cell.summary,
                citation_url: cell.citation_url,
                confidence: cell.confidence,
                guideline: cell.guideline,
            })))
                .sort((a, b) => a.column_id.localeCompare(b.column_id));
            if (cells.length === 0) {
                throw new Error(`Guideline not found: ${guidelineId}`);
            }
            return asTextContent({
                guideline_id: guidelineId,
                guideline: cells[0].guideline,
                cells: cells.map(({ guideline: _guideline, ...cell }) => cell),
            });
        }
        case "list_guidelines":
            return asTextContent(listGuidelines());
        case "list_columns":
            return asTextContent(listColumns());
        default:
            throw new Error(`Unknown tool: ${name}`);
    }
});
(async function main() {
    const transport = new stdio_js_1.StdioServerTransport();
    await server.connect(transport);
})().catch((e) => {
    console.error(e);
    process.exit(1);
});
