# njch-ethics-application

南京市儿童医院 / 南京医科大学附属儿童医院伦理申请材料准备 Skill。

这个 Codex Skill 用于辅助准备院内医学伦理申请材料，尤其适合临床研究伦理初始审查、回顾性病历研究、前瞻性观察研究、免除知情同意、红帆系统填表和提交前材料核查。

> 说明：本项目不是南京市儿童医院官方系统或官方模板发布渠道。伦理材料最终版本、签字、盖章、提交和审查要求应以医院伦理委员会、科研管理系统和伦理办公室的最新要求为准。

## 能做什么

- 梳理伦理申请类型：初始审查、修正方案、年度/定期持续审查、结题报告、SAE、方案违背、暂停/提前终止等。
- 根据研究类型生成材料清单：研究方案、知情同意书、免知情同意申请、招募材料、第三方合作资质、药物/器械说明书等。
- 辅助撰写或修改研究方案、隐私保护、数据安全、风险控制、受益说明和免除知情同意理由。
- 按红帆/院内科研管理系统字段准备可直接粘贴的中文表单内容。
- 对提交前材料进行一致性检查：项目名称、版本号、日期、研究对象、样本量、知情同意路径、附件完整性等。
- 使用本地收录的医院公开模板，并可通过脚本重新抓取公开附件。

## 适用场景

- 南京儿童医院伦理申请
- 临床研究伦理初始审查申请表
- 回顾性病历/数据研究
- 前瞻性观察性研究
- 儿童受试者伦理材料
- 免除知情同意申请
- 红帆系统伦理申请填表
- 药物、医疗器械、体外诊断试剂临床试验相关伦理表格

## 目录结构

```text
njch-ethics-application/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── official-forms/
│       ├── medical-ethics/
│       ├── drug-device-trials/
│       └── manifest.json
├── references/
│   ├── official-sources.md
│   ├── protocol-writing.md
│   ├── redfan-form-fields.md
│   ├── risk-audit.md
│   ├── submission-checklist.md
│   └── waiver-and-privacy.md
└── scripts/
    └── fetch_njch_forms.py
```

## 安装方式

如果使用 Codex Skills，可以把本仓库放到本机的 skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/yuan99999/njch-ethics-application.git ~/.codex/skills/njch-ethics-application
```

之后在 Codex 中使用：

```text
$njch-ethics-application 帮我准备南京儿童医院伦理初始审查材料
```

## 使用示例

```text
$njch-ethics-application
我这个课题是回顾性病历研究，研究对象是 2022-2025 年住院患儿。
请帮我判断需要哪些伦理附件，并起草免除知情同意理由。
```

```text
$njch-ethics-application
请根据我的研究方案，整理红帆系统“临床研究伦理初始审查申请表”每个字段应该填写的内容。
```

```text
$njch-ethics-application
帮我做提交前审查，重点看知情同意、隐私保护、风险控制、附件是否缺失。
```

## 更新医院公开模板

本仓库包含一个模板抓取脚本，用于从已配置的医院公开页面下载附件并更新 `assets/official-forms/manifest.json`：

```bash
python3 scripts/fetch_njch_forms.py
```

也可以指定输出目录进行测试：

```bash
python3 scripts/fetch_njch_forms.py --out /tmp/njch-forms-test
```

运行后应检查 `manifest.json` 中的来源链接、抓取时间和文件列表。不要仅凭本地缓存判断模板一定是最新版本。

## 注意事项

- 不伪造伦理批件、签名、盖章、审批日期、GCP 证书或科室意见。
- 涉及儿童受试者时，应重点说明最小风险、监护人同意、儿童权益保护、隐私保护和额外负担。
- 回顾性研究申请免除知情同意时，应说明不超过最小风险、不会不利影响受试者权益、研究无法实际获得同意或获得同意不可行、隐私保护措施充分。
- 涉及药物、器械、样本、基因检测、数据出境或第三方合作时，应单独核查附件和合规要求。
- 最终提交前，建议与伦理办公室确认当前流程、模板版本和附件要求。

## License

未声明开源许可证前，默认保留所有权利。
