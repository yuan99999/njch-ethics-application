# Official Sources

Use this when verifying hospital pages, source URLs, local template filenames, or whether a template may be stale.

## Hospital Source Pages

- Medical Ethics Committee submission materials:
  `https://www.njch.com.cn/kyjx/detail.asp?ID=5101`
  Page title observed 2026-06-08: `医学伦理委员会送审材料`.
  Observed attachments:
  - `新技术新项目医学伦理申请-知情同意书.doc`
  - `医学伦理申请-研究方案.docx`
  - `医学伦理申请-知情同意书.doc`
  - `医学伦理申请-免知情同意申请.doc`

- Drug clinical trial ethics review material list and templates:
  `https://www.njch.com.cn/kyjx/detail.asp?ID=5401`
  Page title observed 2026-06-08: `药物临床试验伦理审查送审资料清单及模板`.
  Observed attachment categories:
  - Drug and medical device initial review form-review worksheets.
  - Amendment, annual follow-up, noncompliance/protocol deviation, suspension/early termination, and close-out worksheets.
  - Initial ethics review application form for drug/medical-device trials.
  - Amendment application, annual follow-up report, deviation report, SAE report forms, suspension/early termination report, and close-out report.

## Local Template Store

- Local official templates are under `assets/official-forms/`.
- Use `assets/official-forms/manifest.json` to verify filename, source URL, byte size, and fetch time.
- Refresh with:

```bash
python scripts/fetch_njch_forms.py
```

## Regulatory Anchors

- `涉及人的生命科学和医学研究伦理审查办法` (effective 2023-02-18).
- `药物临床试验质量管理规范` (2020), for drug trials.
- `医疗器械临床试验质量管理规范` (2022), for medical device trials.
- Check current PRC personal information protection and data security requirements when identifiable child data, rare-disease data, images, genetic data, or exported/shared data are involved.

## Source Handling

- Cite hospital page URL and fetch date in internal checklists when template currency matters.
- Treat user-provided hospital-issued Word files as authoritative for that submission cycle unless a newer official page contradicts them.
- Leave signature, seal, approval, and committee-use fields blank unless signed/stamped originals are provided.
