# 育见欢喜 · MBTI 人格测试（H5 网页版）

一个纯前端、单文件的 MBTI 16 型人格测试网页，部署后即可对外公开访问，无需后端服务器。

## 功能
- 60 道精选题目，覆盖 E/I、S/N、T/F、J/P 四大维度
- 即时计算 16 种人格类型，给出性格特点、优势、留意点、适合职业方向
- 维度倾向可视化条形图
- 一键复制链接 / 分享结果给朋友
- 支持「上一题 / 下一题」回看与重选（已修复回看重选卡死问题）

## 本地预览
直接双击 `index.html` 即可在浏览器打开；或在本目录起一个静态服务器：

```bash
# Python
python -m http.server 8080
# 然后访问 http://localhost:8080
```

## 部署（GitHub Pages）
1. 把本仓库 push 到 GitHub（已包含 `index.html` 与 `logo.png`）；
2. 进入 GitHub 仓库 → **Settings → Pages**；
3. Source 选 `Deploy from a branch`，Branch 选 `main`、目录 `/ (root)`，点 Save；
4. 等待约 1 分钟，获得公开链接：
   `https://<用户名>.github.io/<仓库名>/`；
5. 将该链接填回小程序 `externalUrl`，替换原有的占位死链。

## 与小程序的对接（预留）
`index.html` 内 `WECHAT_CONFIG` 为小程序跳转预留接口。待小程序 AppID 就绪、将 `enabled` 改为 `true` 后，即可在结果页引导用户跳转小程序保存/对比结果。

## 目录结构
```
.
├── index.html   # 单文件 H5 应用（含全部样式、数据与逻辑）
├── logo.png     # 首页 logo
└── README.md
```

> 本测试基于 MBTI 理论，结果仅供自我探索参考，不构成专业心理建议。
