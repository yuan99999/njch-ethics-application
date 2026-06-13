---
name: njch-ethics-application
description: Prepare, audit, and package 南京市儿童医院/南京医科大学附属儿童医院院内医学伦理申请材料. Use when the user asks about 南京儿童医院伦理申请, 红帆/院内伦理系统填表, 临床研究伦理初始审查, 医学伦理委员会, 临床试验伦理委员会, 回顾性病历研究, 前瞻性研究, 免除知情同意, 研究方案, 知情同意书, 儿童受试者伦理, 隐私保密, 数据安全, 药物或医疗器械临床试验, SAE, 方案违背, 修正方案, 年度跟踪, 结题报告, 伦理附件清单, 模板下载, 或提交前审查.
---

# NJCH Ethics Application

## Core Rules

- Classify the submission first: initial review, amendment, continuing review, close-out, SAE/deviation report, or waiver of informed consent.
- Treat hospital templates as controlling. Preserve their headings, order, signature areas, and committee-use fields.
- Do not fabricate signatures, stamps, approval dates, ethics opinions, GCP certificates, or department approvals.
- For retrospective chart/data studies, explicitly assess whether waiver of informed consent is justified; do not state that waiver approval is guaranteed.
- For pediatric studies, address minimal risk, guardian/child rights, privacy protection, and whether direct contact or extra procedures occur.
- Prefer current hospital templates and source pages over memory. Check `references/official-sources.md` and `assets/official-forms/manifest.json` when template currency matters.
- When producing `.docx`, use the Documents skill and render the Word file to inspect page images before delivery.

## Workflow

1. **Define the study type**
   - Identify whether the project is retrospective, prospective observational, interventional, drug/device, new technology, biospecimen, questionnaire, or data-only.
   - Confirm sites, population age range, data sources, sample size, interventions, extra burden, and consent plan.

2. **Choose the submission package**
   - Read `references/submission-checklist.md` when building a required/optional/confirm-with-office material list.
   - Read `references/official-sources.md` when verifying hospital source pages, local template filenames, or current official attachments.
   - Include a research protocol for all clinical research submissions.
   - Include a waiver form when requesting waiver of informed consent.
   - Include consent/assent materials only when direct participant consent is planned or required.
   - For drug/device/IVD trials or trial follow-up events, separate initial review, amendment, continuing review, deviation/noncompliance, SAE, suspension/termination, and close-out documents.

3. **Draft or revise the protocol**
   - Read `references/protocol-writing.md` before drafting a protocol or editing a hospital protocol template.
   - Keep wording formal, concise, and hospital-facing.
   - Separate routine clinical care from research-only procedures.

4. **Draft waiver and privacy language**
   - Read `references/waiver-and-privacy.md` for waiver justification, minor privacy protection, and data security wording.
   - Use de-identification, limited access, encrypted storage, and aggregate reporting language.

5. **Fill online ethics form**
   - Read `references/redfan-form-fields.md` when the user is filling the 红帆/院内 ethics workflow page.
   - Prefer short, field-ready Chinese wording that fits text boxes and avoids unnecessary research-method detail.

6. **Audit before submission**
   - Read `references/risk-audit.md` for likely committee questions and missing items.
   - Report findings as: `Missing items`, `Ethics risks`, `Suggested wording`, and `Questions for PI`.

7. **Package final files**
   - Use consistent filenames: `项目简称_文件名称_V版本号_YYYYMMDD`.
   - Check version/date consistency across protocol, waiver/consent forms, application forms, and attachments.
   - Remind the user which sections require manual signature or department/PI confirmation.

8. **Refresh official templates when needed**
   - Local official templates live in `assets/official-forms/`.
   - Run `scripts/fetch_njch_forms.py` to refresh attachments from the hospital website.
   - Do not claim a template is current unless the source URL and fetch time are recorded in `assets/official-forms/manifest.json`.

## Bundled Resources

- `assets/official-forms/medical-ethics/`: hospital research protocol, informed consent, waiver of informed consent, and new technology/new project consent templates.
- `assets/official-forms/drug-device-trials/`: drug/device/IVD ethics worksheets and forms for initial review, amendment, annual follow-up, deviation/noncompliance, SAE, suspension/termination, and close-out.
- `scripts/fetch_njch_forms.py`: downloads the latest official attachments from configured NJCH public pages and writes `assets/official-forms/manifest.json`.

## Default Output Style

- Use Chinese unless the user asks for English.
- Be practical and submission-oriented: tell the user exactly what to prepare, what to upload, and what still needs confirmation.
- Keep uncertainty explicit. Use “建议与伦理办公室确认” rather than guessing local administrative requirements.
