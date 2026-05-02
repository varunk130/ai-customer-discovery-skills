#!/usr/bin/env node
// Validates SKILL.md frontmatter across the skills/ directory.
// Required fields: name, version, description, when_to_use, inputs, outputs, tags, maintainer.

const fs = require("fs");
const path = require("path");

const REQUIRED = ["name", "version", "description", "when_to_use", "inputs", "outputs", "tags", "maintainer"];
const SKILLS_DIR = path.join(__dirname, "..", "skills");

function parseFrontmatter(text) {
  const m = text.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!m) return null;
  const block = m[1];
  const fields = new Set();
  for (const line of block.split("\n")) {
    const km = line.match(/^([a-zA-Z_]+):/);
    if (km) fields.add(km[1]);
  }
  return fields;
}

let ok = true;
if (!fs.existsSync(SKILLS_DIR)) {
  console.log("No skills/ directory yet — skipping.");
  process.exit(0);
}

for (const dir of fs.readdirSync(SKILLS_DIR)) {
  const sf = path.join(SKILLS_DIR, dir, "SKILL.md");
  if (!fs.existsSync(sf)) continue;
  const text = fs.readFileSync(sf, "utf8");
  const fields = parseFrontmatter(text);
  if (!fields) {
    console.error(`✗ ${dir}: missing or malformed frontmatter`);
    ok = false;
    continue;
  }
  const missing = REQUIRED.filter((f) => !fields.has(f));
  if (missing.length) {
    console.error(`✗ ${dir}: missing fields → ${missing.join(", ")}`);
    ok = false;
  } else {
    console.log(`✓ ${dir}`);
  }
}

if (!ok) {
  console.error("\nSchema validation failed.");
  process.exit(1);
}
console.log("\nAll skills valid.");