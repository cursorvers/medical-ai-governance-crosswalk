#!/usr/bin/env node
"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const lookup_index_json_1 = __importDefault(require("./lookup-index.json"));
const typedCorpus = lookup_index_json_1.default;
const RED = "\x1b[31m";
const YELLOW = "\x1b[33m";
const GRAY = "\x1b[90m";
const DIM = "\x1b[2m";
const BOLD = "\x1b[1m";
const CYAN = "\x1b[36m";
const RESET = "\x1b[0m";
function strengthColor(s) {
    switch (s) {
        case "must":
            return RED;
        case "should":
            return YELLOW;
        case "mention":
            return GRAY;
        case "none":
            return DIM;
        case "not_assessed":
            return GRAY;
        case "source_unavailable":
            return DIM;
    }
}
function pad(value, width) {
    return value.padEnd(width, " ");
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
function printHelp() {
    console.log(`Usage: medgov [options] <query>

Commands:
  <query>              Search columns and guideline cells
  --list-columns       List columns A-M
  --list-guidelines    List guideline IDs and names

Options:
  --json               Emit JSON for search and list commands
  --help, -h           Show this help`);
}
function parseArgs(argv) {
    const positional = [];
    let help = false;
    let json = false;
    let shouldListColumns = false;
    let shouldListGuidelines = false;
    for (const arg of argv) {
        if (arg === "--help" || arg === "-h") {
            help = true;
        }
        else if (arg === "--json") {
            json = true;
        }
        else if (arg === "--list-columns") {
            shouldListColumns = true;
        }
        else if (arg === "--list-guidelines") {
            shouldListGuidelines = true;
        }
        else {
            positional.push(arg);
        }
    }
    return {
        help,
        json,
        listColumns: shouldListColumns,
        listGuidelines: shouldListGuidelines,
        query: positional.join(" "),
    };
}
function main() {
    const argv = process.argv.slice(2);
    const args = parseArgs(argv);
    if (argv.length === 0 || args.help) {
        printHelp();
        process.exit(0);
    }
    if (args.listColumns) {
        const columns = listColumns();
        if (args.json) {
            console.log(JSON.stringify(columns, null, 2));
        }
        else {
            for (const column of columns) {
                console.log(`${column.id}  ${column.name} — ${column.name_en}  (${column.cell_count} cells)`);
            }
        }
        process.exit(0);
    }
    if (args.listGuidelines) {
        const guidelines = listGuidelines();
        if (args.json) {
            console.log(JSON.stringify(guidelines, null, 2));
        }
        else {
            for (const guideline of guidelines) {
                console.log(`${guideline.guideline_id} — ${guideline.guideline}`);
            }
        }
        process.exit(0);
    }
    const matches = search(args.query);
    if (args.json) {
        console.log(JSON.stringify({ query: args.query, match_count: matches.length, matches }, null, 2));
        process.exit(0);
    }
    if (matches.length === 0) {
        console.log(`${DIM}(no matches for '${args.query}')${RESET}`);
        process.exit(1);
    }
    matches.forEach((match, index) => {
        if (index > 0) {
            console.log("");
        }
        console.log(`${BOLD}${CYAN}${match.column_id} — ${match.column_name} (${match.column_name_en})${RESET}`);
        for (const cell of match.cells) {
            console.log(`  [${strengthColor(cell.strength)}${pad(cell.strength, 7)}${RESET}] ${cell.guideline}`);
            console.log(`            ${cell.summary}`);
            console.log(`            ${DIM}${cell.citation_url}${RESET}`);
        }
    });
    process.exit(0);
}
main();
