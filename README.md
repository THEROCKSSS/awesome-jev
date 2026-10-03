# Awesome Jev

A community catalog of Jev / TypeSafe System One projects — models, SDKs, agents, MCP tools and experiments. The repository list is refreshed by a daily GitHub Action. Each detail page loads that project's original README from GitHub when opened.

⭐ **[Explore the interactive catalog →](https://therocksss.github.io/awesome-jev/)** — scroll through the landscape, filter the full list, then open a dedicated page for any repository.

Catalog metadata is a **NON-LIVE DATA** snapshot; the project README on each detail page is **LIVE DATA** from the GitHub API. The README is attributed to its original repository. If GitHub blocks a request or a repo has no README, the page links directly to the original. [Share the catalog](docs/SHARE.md) with someone who would use it.

Jev is TypeSafe's *System One* family: fast, cheap, typed decision models that pick an action instead of generating prose. This list collects everything the community has built around it — official tooling, open reimplementations, and applications — in one place.

## Contents

- [Official Resources](#official-resources)
- [Open & Jev-like Models](#open--jev-like-models)
- [SDKs, APIs & Routers](#sdks-apis--routers)
- [Agents & Automation](#agents--automation)
- [MCP & Agent Tools](#mcp--agent-tools)
- [Web & Browsing](#web--browsing)
- [Developer Tools](#developer-tools)
- [Games & Play](#games--play)
- [Chat & Messaging](#chat--messaging)
- [Finance & Trading](#finance--trading)
- [Safety, Routing & Guardrails](#safety-routing--guardrails)
- [Productivity & Knowledge](#productivity--knowledge)
- [Media & Content](#media--content)
- [Mobile & Desktop Apps](#mobile--desktop-apps)
- [Home, IoT & Robotics](#home-iot--robotics)
- [Awesome Lists & Catalogs](#awesome-lists--catalogs)
- [More Projects](#more-projects)

<!-- PROJECTS:BEGIN -->

### 🆕 New today (2026-10-03)

- [jevbox](https://github.com/extend-hq/jevbox) —  _(★140)_
- [dsh-jev-plugin](https://github.com/luobosibing2/dsh-jev-plugin) — Native DeepSeek Harness (DSH) plugin integrating TypeSafe Jev as a System One decision layer for agent selection, supervision, corrections, and approvals. _(★90)_
- [social-monitor](https://github.com/777genius/social-monitor) — Tired of scrolling through hundreds of near-identical posts across every social network just to find the few that actually matter. Instead of drowning in duplicate takes, reposts, and filler from X, Reddit, news sites, I wanted one tool tha _(★48)_
- [atoma](https://github.com/mgtf/atoma) — Watch a request turn into finished work. AI agents produce and check it; TypeSafe's Jev decides. _(★16)_
- [pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router) — Route pi prompts to task-appropriate model tiers with TypeSafe Jev typed judgments. Budget-aware, with automatic fallback. _(★11)_
- [jev-permission-gate](https://github.com/madisonrickert/jev-permission-gate) — A Claude Code mod that uses TypeSafe's Jev to decide auto mode tool calls. 2x faster than the built-in classifier on the calls it decides. _(★10)_
- [jev-docs](https://github.com/chenrui333/jev-docs) — Community-maintained history of Jev / TypeSafe System One APIs, SDKs, agent guidance, and engineering best practices. _(★5)_
- [zero-shot-ie-bench](https://github.com/umstek/zero-shot-ie-bench) — 60 zero-shot information-extraction & classification systems (57 benchmarked) across 32 families — extractor encoders, zero-shot classifiers, cross-encoder rerankers, typed-decision engines — local, Ollaya-served & hosted (OpenRouter, Cloud _(★4)_
- [sedum](https://github.com/sedum-dev/sedum) — Plain-English browser e2e tests cheap enough to run on every PR. Built on Jev and Playwright, open source, bring your own key. _(★3)_
- [RSI-Jev-Slay-the-Spire-2](https://github.com/yzxoi/RSI-Jev-Slay-the-Spire-2) —  _(★3)_
- [decidealot](https://github.com/psyb0t/decidealot) — Local decision models for typed choices, scores, and yes-no calls. Run Laya, Von, and CLM through TypeSafe-compatible HTTP and MCP. _(★3)_
- [anofox-decide](https://github.com/DataZooDE/anofox-decide) — DuckDB extension: evaluate natural-language predicates and answer sets with TypeSafe Jev or local open decision models (Julia-1, Laya) _(★2)_
- [pi-smart-subagents](https://github.com/awoaCrim/pi-smart-subagents) — Pi subagents with Jev model and tool routing, worktree isolation, and background task management. _(★2)_
- [ajevt-browser](https://github.com/XYenon/ajevt-browser) — A bounded Jev System-1 browser tool for Pi, OpenCode V2, Amp, and MCP, powered by agent-browser _(★2)_
- [JEV-FROM-SCRATCH](https://github.com/Binny-Shukla/JEV-FROM-SCRATCH) —  _(★1)_
- [kleene](https://github.com/keyboardsamurai/kleene) — Kotlin library for typed model judgments: yes/no, pick-one and rating answers from Jev-style models. Your Policy decides; UNKNOWN is a value. _(★1)_
- [jev_uav](https://github.com/dym397/jev_uav) —  _(★1)_
- [vlm-decision-classifier](https://github.com/Yumeno/vlm-decision-classifier) — ローカルVLMに選択肢の記号1文字で答えさせ、1トークン目の確率で画像を分類する Jev 風の選択式判定の技術検証(llama.cpp / Windows) _(★1)_
- [wagtail-jev](https://github.com/rinti/wagtail-jev) — Use jev to classify tags for pages _(★1)_
- [jev-decision](https://github.com/Coding-Dev-Tools/jev-decision) — Zero-dependency System 1 decision engine, calibrated guardrails, and token optimization client for Jev (TypeSafe AI) _(★1)_
- [nl-jev-decision-gates-expense-policy](https://github.com/ElliotOne/nl-jev-decision-gates-expense-policy) — A production-shaped Python example of using Jev as a typed semantic decision layer inside a deterministic expense-policy workflow. _(★1)_
- [decision-model-sdk-rust](https://github.com/zchee/decision-model-sdk-rust) — Unofficial async Rust SDK for the TypeSafe AI System One API: typed questions via #[derive(QuestionSet)], a port of typesafe-sdk-python. _(★1)_
- [kev](https://github.com/joezxh/kev) — kev like jev _(★0)_
- [last-lst97-dev](https://github.com/lst97-oss/last-lst97-dev) — Simple personal profolio plus chat assistance with RAG and Jev 🇦🇺🇭🇰 _(★0)_
- [jevpilot](https://github.com/bloudhood/jevpilot) — MCP server that gives agents a browser that finishes tasks itself: Jev plans each step, real Chrome executes, results come back verified. _(★0)_
- [openfront-agent](https://github.com/mogottsch/openfront-agent) — A local OpenFront agent using TypeSafe Jev for bounded gameplay decisions. _(★0)_
- [JEV-automation](https://github.com/jjmrock/JEV-automation) —  _(★0)_
- [fastcampus-jev](https://github.com/teddylee777/fastcampus-jev) —  _(★0)_
- [chat-jev-mac](https://github.com/buildforpeople4iv/chat-jev-mac) — 聊天消息意图与风险识别助手：macOS 悬浮窗（微信）+ Chrome 扩展（网页端聊天）。纯只读，不注入、不自动发送。 _(★0)_
- [JEVArena](https://github.com/pouramin/JEVArena) —  _(★0)_
- [jev-hooks](https://github.com/7hemas7er/jev-hooks) — Claude Code commit reviewer driven by Jev-style typed decisions, with a measured question bench (self-hosted rizzo-flow or TypeSafe Jev) _(★0)_
- [jev-trader](https://github.com/gilesknap/jev-trader) —  _(★0)_
- [jev-sinhala-review](https://github.com/Azri-Muhsin/jev-sinhala-review) —  _(★0)_
- [good-cop](https://github.com/timainge/good-cop) — A second opinion on every tool call your coding agent makes: local-first guardrails for Claude Code and Codex, with LLM, decision-model (Jev) and local judges, and backtesting on your own sessions. _(★0)_
- [jevvi-portfolio](https://github.com/jevvis/jevvi-portfolio) —  _(★0)_
- [jevx](https://github.com/bas65u17e8/jevx) — content _(★0)_
- [astrbot_plugin_jev_active_reply](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply) — Jev主动回复插件 · 作者木有知 · TypeSafe/MindsHub多Key与同人连续补充合并 _(★0)_
- [jev-ai-emails-flow](https://github.com/tarunchandel/jev-ai-emails-flow) — AI-powered email flow automation _(★0)_
- [jev-ultrafast-computer-use](https://github.com/dovstern/jev-ultrafast-computer-use) — Supervised Jev browser use for Codex and Claude _(★0)_
- [jevng](https://github.com/willow8939/jevng) — content _(★0)_
- [latent-vla-jev](https://github.com/zhangzhongbo2213/latent-vla-jev) —  _(★0)_
- [jev-a2a](https://github.com/skhlo/jev-a2a) — Jev router: a prompt with an envelope and a record, across Paseo hosts _(★0)_
- [Support-Ticket-Ai-Agent-with-RAG-Guardrails-and-Jev](https://github.com/AlienXc137/Support-Ticket-Ai-Agent-with-RAG-Guardrails-and-Jev) — An agent that reads incoming student queries (email/WhatsApp/form text), classifies them (refund, batch access, payment, technical, academic doubt), drafts a reply from a knowledge base, and decides: auto-reply or escalate to a human. _(★0)_
- [tomorrow-family](https://github.com/imranrkhan13/tomorrow-family) — Fictional prescription-reading demo: source-linked readings with separate Jev and Lev text checks. Human review required; not medical advice. _(★0)_
- [jev-terminal-browser-driver](https://github.com/nedzen/jev-terminal-browser-driver) — Hermes plugin: drive and read a visible terminal-browser tab with Jev typed decisions. No screenshots, fractions of a cent per step. _(★0)_
- [jev_abstract_screener](https://github.com/gelob33/jev_abstract_screener) —  _(★0)_
- [opencode-jevlint](https://github.com/codegirl-007/opencode-jevlint) —  _(★0)_
- [Jev-decision-control](https://github.com/maanik-chandela/Jev-decision-control) — Research framework for evaluating calibration, stability, robustness, and computation control in decision-native AI models. _(★0)_
- [GhidraExportToJson](https://github.com/AntoNainRatio/GhidraExportToJson) — Ghidra script for exporting functions to JSON format. Used in a context of experiment upon Siftrank (using jev AI) _(★0)_
- [ComfyUI-SystemOne](https://github.com/dante01yoon/ComfyUI-SystemOne) — ComfyUI nodes that branch workflows on natural-language judgments from System One models (local Laya or hosted Jev) _(★0)_
- *38 more on the [full catalog](https://therocksss.github.io/awesome-jev/)*

### Official Resources (17)

- [skills](https://github.com/typesafe-ai/skills) — Agent skills for building with TypeSafe's System One API _(★2544, n/a)_
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — The official TypeScript/JavaScript library for the TypeSafe API _(★266, TypeScript)_
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — The official Python library for the TypeSafe API _(★263, Python)_
- [daggerverse](https://github.com/typesafe-ai/daggerverse) — Collection of useful Dagger modules _(★24, Python)_
- [typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go) — Go SDK for the TypeSafe AI API — typed questions in, probability distributions out. _(★9, Go)_
- [typesafe-sdk](https://github.com/joshmn/typesafe-sdk) — Ruby client for typesafe.ai _(★8, Ruby)_
- [typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java) — Community Java SDK for Jev, TypeSafe's System One model: typed questions in, typed answers with calibrated probabilities out. Java 17+, Spring Boot starter (unofficial) _(★7, Java)_
- [typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift) — Unofficial Swift library for the TypeSafe API _(★5, Swift)_
- [typesafe-sdk-rust](https://github.com/codeitlikemiley/typesafe-sdk-rust) — Rust SDK for the TypeSafe AI API _(★4, Rust)_
- [typesafe-sdk-swift](https://github.com/InsaneArts/typesafe-sdk-swift) — Swift SDK for TypeSafe AI _(★4, Swift)_
- [typesafe-ai-java](https://github.com/jamilxt/typesafe-ai-java) — Community-maintained Java SDK for the TypeSafe AI System One (Jev) API. Not an official TypeSafe product. _(★4, Java)_
- [typesafe-sdk](https://github.com/binnash/typesafe-sdk) — PHP & Laravel SDK for TypeSafe AI's JEV Model series _(★3, PHP)_
- [typesafe-sdk-go](https://github.com/valksor/typesafe-sdk-go) — Unofficial Go SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI. _(★1, Go)_
- [typesafe-sdk-php](https://github.com/valksor/typesafe-sdk-php) — Unofficial PHP SDK for the TypeSafe AI System One API — 1:1 parity with the official JS and Python SDKs. Not affiliated with TypeSafe AI. _(★1, PHP)_
- [typesafe-sdk-go](https://github.com/jmelahman/typesafe-sdk-go) — Unofficial Golang library for the TypeSafe API _(★1, Go)_
- [typesafe-sdk-rust](https://github.com/zchee/typesafe-sdk-rust) — Unofficial async Rust SDK for the TypeSafe AI System One API: typed questions via #[derive(QuestionSet)], a port of typesafe-sdk-python. _(★1, Rust)_
- [typesafe-sdk-go](https://github.com/guchengod/typesafe-sdk-go) — Go SDK for TypeSafe AI — classification and rating primitives over text and JSON _(★1, Go)_

### Open & Jev-like Models (475)

- [laya](https://github.com/NandhaKishorM/laya) — Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ languages, with a router that picks the right checkpoint per request. _(★30327, Python)_
- [kev](https://github.com/jaredpalmer/kev) — Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on your own _(★8344, Python)_
- [laya-mlx](https://github.com/mizorewww/laya-mlx) — Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text generation, PyTorch, or cloud API. _(★6284, Python)_
- [semif](https://github.com/TheoLeeCJ/SemIf-OpenJev) — Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe. _(★4668, Python)_
- [nanojev](https://github.com/TianyuCodings/NanoJev) — A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline. _(★2479, Python)_
- [jeff](https://github.com/firelex/jeff) — Millisecond decisions, any domain: a 0.8B open "System 1" model that picks between your options with calibrated probabilities. One base, swappable LoRA adapters, on your own hardware. _(★1338, Python)_
- [jev](https://github.com/feder-cr/jev) — jevos is an open-source alternative to Jev for yes/no decisions that runs on your laptop. _(★1191, Python)_
- [ollaya](https://github.com/ollaya-dev/ollaya) — Run open decision models locally: pull and serve Laya, decider, NLI and GLiClass behind a TypeSafe-compatible API. Ollama for decision models. _(★1144, Rust)_
- [decider](https://github.com/Mapika/decider) — A family of System One-style models fine-tuned from Qwen3.5, designed for one-pass typed decisions with calibrated probabilities. _(★1048, Python)_
- [anyjev](https://github.com/nokia-applied-research/AnyJev) — Turn any LLM into a Jev-style decision model: typed decisions, real probabilities, no training. (continue updating) _(★1018, Python)_
- [deepopen](https://github.com/deepopen-com/deepopen) — 非自回归System 1决策引擎，专为结构化类型决策场景设计  DeepOpen Multilingual, non-autoregressive System 1 decision engine. _(★1014, Python)_
- [typellm](https://github.com/TypeLLM/TypeLLM) — TypeLLM: LLMs with type-safe generation _(★913, Python)_
- [von](https://github.com/wfzyx/von) — The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev. _(★821, Python)_
- [rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) — The open, local take on Jev: typed decisions from an LLM, without generating a single token _(★800, Python)_
- [laya](https://github.com/receptron/laya) — Run Laya, the open-source Jev-compatible System-1 decision model, from Node.js / TypeScript via ONNX Runtime _(★737, TypeScript)_
- [openjev](https://github.com/razorback16/openjev) — Open, Jev-compatible System One decision server on DiffusionGemma _(★592, Python)_
- [simple-jev](https://github.com/featherless-ai/simple-jev) — Turn any open model into a classifier/jev endpoint _(★582, Python)_
- [valen](https://github.com/Liuziyu77/Valen) — Train a Jev-like multimodal model by yourself. System One Model, now with vision. _(★578, Python)_
- [docjev](https://github.com/jerryjliu/docjev) — A very fast document classifier/splitter using Jev _(★498, Python)_
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page. _(★492, TypeScript)_
- [jeeves](https://github.com/PostHog/jeeves) — Jeeves – Reasoning improves Jev-like decision models _(★400, Python)_
- [Open-Jev](https://github.com/Zefan-Cai/Open-Jev) —  _(★389, Python)_
- [llm2jev](https://github.com/Yinsongxu/LLM2Jev) — Turn local language models into Jev-style structured decision models. Get results from text and images with prefill alone—no token-by-token decoding required. _(★386, Python)_
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — Drop-in TypeSafeClient replacement backed by LLM APIs _(★377, Python)_
- [system-one-connector](https://github.com/itsmostafa/system-one-connector) — System One MCP connector to evaluate anything fast and cheap. Give your AI agent direct access to models like: Typesafe AI's Jev model and Laya _(★340, Go)_
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) — Jev-compatible API endpoint based on open models (prefill-only) _(★337, Python)_
- [openjev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) — Calibrated 151M Non-Autoregressive Decision Engine beating TypeSafe Jev & Laya on LocalLLaMA/typed-decisions (77.10% acc, 0.0636 Brier, 0.0144 ECE) _(★293, Python)_
- [jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision) — Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex Harness。 _(★252, JavaScript)_
- [killmyidea](https://github.com/monteduro/killmyidea) — Describe your startup idea. Jev decides: kill it, fix it or ship it. _(★249, TypeScript)_
- [laya-ultrafast](https://github.com/ipenywis/laya-ultrafast) — Same as jev-ultrafast but using Laya _(★244, Python)_
- [vllm-jev](https://github.com/mode-io/vllm-jev) — Native vLLM serving for Jev decision models _(★231, Python)_
- [jevpilot](https://github.com/standardagents/jevpilot) — A playable Three.js driving simulator with Jev-powered autopilot _(★208, JavaScript)_
- [jevbench](https://github.com/fstandhartinger/jevbench) — JevBench v1 - a benchmark for Jev-class typed decision models: smart, cheap, fast, reliable, open. _(★206, Python)_
- [tev1](https://github.com/togethercomputer/tev1) — Open-weight, Jev-inspired decision model finetuned on top of Qwen3.5 4B _(★205, Python)_
- [systemoneharness](https://github.com/HarnessRouter/SystemOneHarness) — The system one Harness for system one models _(★194, Python)_
- [openjev](https://github.com/SiliconLabAI/OpenJev) — OpenSource Jev _(★164, TypeScript)_
- [neo4jev](https://github.com/jexp/neo4jev) — Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships _(★157, Jupyter Notebook)_
- [reflex](https://github.com/kshetrajna12/reflex) — A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5. _(★153, Python)_
- [jev-mem](https://github.com/libingzheren/Jev-Mem) — Jev-Mem: System-One Controlled Agentic Memory _(★146, Python)_
- [jevk5](https://github.com/allebee/jevk5) — JevK5: open-weight alternative to TypeSafe Jev. Typed decisions with probabilities in one forward pass; Apache-2.0 weights and code. _(★132, Python)_
- [open-jev](https://github.com/daseinlabs/open-jev) — Open Jev implementation with custom finetuning _(★123, Python)_
- [verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) — Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground _(★110, Python)_
- [jev-arena](https://github.com/NanmiCoder/jev-arena) — Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、原速回放与离线报告。 _(★103, JavaScript)_
- [winnow](https://github.com/GhalebDweikat/winnow) — A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context. _(★102, Python)_
- [jevcore](https://github.com/PerryLink/jevcore) — TypeSafe Jev for DeepSeek Harness, the Model Context Protocol, and plain Node: typed judgments instead of prose, offline by default. _(★102, TypeScript)_
- [laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev) — Laya vs Jev: local MLX and hosted AI decisions playing T-Rex side by side, with live metrics and replay recording _(★99, Python)_
- [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) — High-throughput synthetic and pretraining dataset sifter for TypeSafe Jev. Rust streaming core, Parquet and JSONL I/O, typed Choice/Score/Noul judgments, speculative fan-out, 24.0 rows/sec measured. _(★97, Rust)_
- [laya-server](https://github.com/1Panel-dev/laya-server) — A self-hosted API and web interface for Laya’s structured decision models, compatible with the TypeSafe Jev API format. _(★87, TypeScript)_
- [jevfire](https://github.com/kikoncuo/jevfire) — JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, and reproducible benchmarks. _(★72, JavaScript)_
- [james_library](https://github.com/topherchris420/james_library) — R.A.I.N. Lab is an experimental scientific-agent architecture that separates fast local judgment, independent probabilistic evaluation, multi-agent deliberation, evidence, and authorization into distinct computational layers.🐙(Predates Karp _(★72, Rust)_
- *425 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### SDKs, APIs & Routers (121)

- [jev-gateway](https://github.com/vinilana/jev-gateway) — An easy way to use jev with your coding agent for tool calling reasoning _(★287, TypeScript)_
- [quackd](https://github.com/rokbenko/quackd) — One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain (Claude, OpenAI, Gemini, Grok, or local via Ollama or vLLM) and a decision LLM for multiple choice (Jev, Laya, Kev). Drives Mi _(★247, Python)_
- [jev-social](https://github.com/socai-io/jev-social) — Jev × socai turns a social research question into real Instagram, TikTok, and LinkedIn evidence plus a source-linked report. _(★142, JavaScript)_
- [neurolink](https://github.com/juspay/neurolink) — The pipe layer of an AI nervous system — one interface connecting provider neurons to your application, across three inference types: generate, stream, and a calibrated decide (via TypeSafe Jev). MCP-native, voice (TTS/STT/realtime), RAG, m _(★142, TypeScript)_
- [jgrep](https://github.com/keltokhy/jgrep) — grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line. _(★134, Python)_
- [jevmail](https://github.com/fazlerocks/jevmail) — Open-source AI email triage for Gmail. Sorts your inbox into Needs reply, Updates, Promos, Sales and Spam with Jev, TypeSafe AI's decision model, via Vercel AI Gateway. Read-only, runs locally, 1,000 emails in about a minute for 3 cents. _(★93, TypeScript)_
- [warrenduffer](https://github.com/arimanyus/warrenduffer) — AI-driven intraday trading bot for Indian stocks. Jev ranks the Nifty 50 every 15s; code sizes each trade and places the stop; orders go live through Zerodha Kite or Kotak Neo. Day replay, kill switch, daily loss halt, terminal dashboard. _(★93, TypeScript)_
- [stuntd](https://github.com/bladedevoff/stuntd) — Local proxy that learns your app's typed LLM decisions and answers them with a Laya head. Jev and OpenAI compatible. _(★61, Python)_
- [spring-ai-typesafe](https://github.com/spring-ai-community/spring-ai-typesafe) — A Java SDK for the TypeSafe AI JEV API, & Spring AI TypeSafe integrations. _(★47, Java)_
- [jevbridge](https://github.com/tacticocc/Jevbridge) — ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode. _(★43, TypeScript)_
- [jev-edge](https://github.com/kiwi0719/jev-edge) — Typed-judgment admission control at the traffic edge: three-layer prompt-injection and abuse filter for nginx/OpenResty, powered by TypeSafe Jev. Fail-open, cached, hot-reloadable. _(★40, Lua)_
- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) — This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev. _(★39, TypeScript)_
- [jev-cua](https://github.com/ronadin2002/jev-cua) — Voice and text control for macOS. One floating bar, live UI action selection with Jev, and a continuous observe–act–verify loop. _(★36, Swift)_
- [jev-for-chrome](https://github.com/chy4pro/jev-for-chrome) — Jev for Chrome: drives the tab you are looking at with TypeSafe Jev, a sub-second decision model. Community port of browser-use/jev-ultrafast, not affiliated with TypeSafe. _(★35, TypeScript)_
- [jev-calibrate](https://github.com/smkrv/jev-calibrate) — Calibrate Jev questions against your own labels: tune criteria on labelled examples, confirm on a held-out set, get a verdict per question. Unofficial. _(★32, TypeScript)_
- [typesafe](https://github.com/krzyzanowskim/TypeSafe) — TypeSafe SDK in Swift _(★28, Swift)_
- [yoshi](https://github.com/compozy/yoshi) — Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy _(★26, TypeScript)_
- [jsort](https://github.com/keltokhy/jsort) — sort by meaning: order lines along a plain-English dimension, from pairwise comparisons judged by TypeSafe's Jev model _(★26, Python)_
- [go-jev](https://github.com/mattn/go-jev) — Go SDK and CLI for TypeSafe Jev: typed decisions (yes/no, choice, score) from a model _(★25, Go)_
- [ulka](https://github.com/razaanstha/ulka) — Experimental browser agent powered by FX, Jev, and Vercel AI Gateway. Bring your own API key to read pages and automate browser tasks. _(★24, TypeScript)_
- [evoke](https://github.com/evoke-build/evoke) — Software, by reflex. Say it, and the right small program runs: chosen by a calibrated classifier, run only when it is sure enough, and it asks before anything that cannot be undone. A CLI, a package manager and a TypeScript SDK: the first i _(★22, Rust)_
- [fastjev](https://github.com/chengyongru/fastjev) — SDK-first, independently maintained SemIf fork for fast, self-hosted semantic decisions. _(★21, Python)_
- [notjev](https://github.com/9pings/notjev) — Super fast Jev like server, model agnostic, working with any OpenAI compatible endpoint _(★20, JavaScript)_
- [cheshi](https://github.com/CheshiAI/Cheshi) — Jev-powered conversation memory: find past sessions and revisit decisions with original sources. A macOS workspace for OpenAI Codex. Manage AI conversations and agents, explore code with CodeGraph, and work with Git, Ghostty terminals, and  _(★18, C)_
- [jevper](https://github.com/zhulinchng/jevper) — Jev-shaped (TypeSafe System One) classification wrapper over OpenAI-like clients _(★17, Python)_
- [swift-jev](https://github.com/d-date/swift-jev) — A Swift client for TypeSafe AI's Jev — typed judgements, not text _(★16, Swift)_
- [swift-typesafe](https://github.com/ainame/swift-typesafe) — Unofficial Swift SDK for TypeSafe _(★15, Swift)_
- [prompture](https://github.com/jhd3197/Prompture) — Prompture is an API-first library for requesting structured JSON output from LLMs (or any structure), validating it against a schema, and running comparative tests between models. _(★14, Python)_
- [typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) — Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI. _(★13, C#)_
- [jev](https://github.com/stefafafan/jev) — An unofficial, provider-neutral Unix client for Jev from TypeSafe AI. Written in Go. _(★13, Go)_
- [switchboard](https://github.com/ruban-24/switchboard) — An open-source, model-agnostic decision router for Claude Code and Codex. _(★12, TypeScript)_
- [jevcache](https://github.com/kushals256/jevcache) — MorrowCache — skip the chat call when the question is the same. OpenAI-compatible proxy. npm: @kushalicious/jevcache _(★12, TypeScript)_
- [jev](https://github.com/okooo5km/jev) — Typed decisions from the shell: an unofficial stdlib-Python CLI and Agent Skill for TypeSafe's Jev model, via the TypeSafe API (default) or OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch _(★10, Python)_
- [omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction) — Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter _(★9, TypeScript)_
- [flue-jev-demo](https://github.com/matthewp/flue-jev-demo) — Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway _(★9, TypeScript)_
- [jevymarket](https://github.com/markusbug/jevymarket) — Polymarket trading bot driven by Jev (TypeSafe AI) via OpenRouter _(★9, Python)_
- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) — Can a decision model beat dedicated rerankers? TypeSafe Jev vs Cohere Rerank 4 vs ZeroEntropy zerank-2 vs a chat-model baseline: 14 datasets, every raw API response, bootstrap ranges on every gap. _(★8, Python)_
- [diffjury](https://github.com/raihankhan-rk/diffjury) — DiffJury — TypeSafe Jev PR risk router + code review coach _(★8, TypeScript)_
- [jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK) — An independent, type-safe Swift SDK for TypeSafe Jev, with async/await, batching, retries, and SPM support. _(★8, Swift)_
- [jev-compact](https://github.com/fatelei/jev-compact) — Jev-scored context compaction for OpenAI Codex CLI — scores every tool call before compaction and restores critical tool outputs verbatim after it _(★8, TypeScript)_
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) — Independent calibration test of TypeSafe's Jev on a task it cannot have seen: 900 rule-generated support tickets (choice / score / boolean) plus 3 public benchmarks via Vercel AI Gateway. Raw responses, ECE with noise floor, temperature ref _(★7, Python)_
- [jev-canvas](https://github.com/gaborishka/jev-canvas) — Draw on a tldraw canvas with your voice and a pointing finger. Jev (TypeSafe System One) decides action, target and place in ~350 ms per spoken word. _(★7, JavaScript)_
- [jevtown](https://github.com/gaborishka/jevtown) — Jevtown: a social network where people write and 10,000 AI personas react _(★7, JavaScript)_
- [jev-harness](https://github.com/ismaelsoilet/jev-harness) — Zero-dependency System One decision harness: 5 semantic gates saving frontier AI agent tokens on trivial errors & doom loops. Python + TypeScript + Rust. MCP-compatible. _(★7, Python)_
- [scala-jev-sdk](https://github.com/ticofab/scala-jev-sdk) — Scala SDK for Jev. No effect system bundled. _(★7, Scala)_
- [jevgo](https://github.com/devbackend/jevgo) — Unofficial Go client for the TypeSafe AI System One API (Jev) — typed questions in, calibrated answers out. _(★7, Go)_
- [jev-architect](https://github.com/karanb192/jev-architect) — Find, design, and evaluate TypeSafe Jev decision loops. _(★7, HTML)_
- [jevc](https://github.com/doronp/jevc) — Compile agent policy prose into deterministic verdict programs: narrow evidence questions for the model, the verdict computed in code. Install: npm i -g jev-compiler _(★7, TypeScript)_
- [typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs) — Independent async and blocking Rust SDK for the TypeSafe AI System One API _(★6, Rust)_
- [typesafe_sdk](https://github.com/nshkrdotcom/typesafe_sdk) — An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is t _(★6, Elixir)_
- *71 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Agents & Automation (178)

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — Fastest and cheapest web agent _(★21853, Python)_
- [reticle](https://github.com/reticlehq/reticle) — AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications. _(★1150, TypeScript)_
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — Computer use for about $0.0002 a step: OCR the screen, classify the next action with TypeSafe, click. macOS. _(★1149, Python)_
- [learn-agent-architecture](https://github.com/hardness1020/learn-agent-architecture) — Learn AI agents from scratch. _(★1038, Python)_
- [hippo-memory](https://github.com/kitfunso/hippo-memory) — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in hosted TypeSafe Jev reranker. _(★770, TypeScript)_
- [jevrev](https://github.com/Alex314618-create/JevRev) — An LLM + Jev workflow that changes EVERYTHING. Boost your vertebrate brain with a spine inside. _(★703, TypeScript)_
- [foreman](https://github.com/thruwire/foreman) — Software factory foreman based on TypeSafe's Jev model _(★658, Python)_
- [agent](https://github.com/AgentiLoop/Agent) — AgentiLoop Agent! — One app. Any AI. Your Mac, working for you. Native Swift agent for Mac: drives any app via Accessibility, codes/builds in Xcode, automates AppleScript, JXA, Swift and SMAppService shell (user/root). 23 LLM providers, loc _(★640, Swift)_
- [vexjoy-agent](https://github.com/notque/vexjoy-agent) — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop. _(★425, Python)_
- [agent-jev](https://github.com/malevrigns/agent-jev) — AgentJev-0.6B - a fast 'System One' decision model for AI Agents: feed it any unstructured state (diffs, traces, logs) and structured questions, get calibrated probability distributions back in one ~50ms forward pass. Zero output-token deco _(★337, Python)_
- [beebots](https://github.com/imikerussell/beebots) — Three AI trading bees on OKX, every decision by Jev. Paper trading by default. Not financial advice. _(★220, TypeScript)_
- [ten-levels-of-jev](https://github.com/disler/ten-levels-of-jev) — Ten levels of Jev, from one smart if statement to a coding agent that reaches for Jev on its own _(★163, TypeScript)_
- [pi-jev](https://github.com/y0usaf/pi-jev) — TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers _(★154, TypeScript)_
- [jev-workflow-builder](https://github.com/CTNicholas/jev-workflow-builder) —  _(★149, TypeScript)_
- [supercov](https://github.com/supercorp-ai/supercov) — Coverage, security and code quality for coding agents _(★144, Rust)_
- [webctl](https://github.com/dorkitude/webctl) — Smart web search CLI for agents, backed by Jev. Saves a lot of tokens. _(★143, Go)_
- [jev-engineering-zh](https://github.com/yibie/jev-engineering-zh) — 《Jev 工程学：为 coding agent 而作》完整中文翻译 — 保留原结构与 7 张插图 _(★134, n/a)_
- [jevry](https://github.com/michaelswissa/jevry) — Your browser. Ready to act. An MIT-licensed desktop browser agent for website tasks, cited research, and supported games. _(★118, TypeScript)_
- [agentic-rl](https://github.com/cookiespiggy/agentic-rl) — Agentic RL 中文零基础教程（25 章）：从概念到 GRPO 实战，含 TRL 最小可跑示例。第 25 章讲清 Jev / TypeSafe System One 判别模型与 RL 的能力边界 | Chinese Agentic RL tutorial, 25 chapters + Jev-vs-RL boundary analysis _(★116, Python)_
- [jev-use](https://github.com/savka777/jev-use) — Say it, and your Mac does it. A computer-use harness on Jev that reads the screen through Accessibility. Fast, no vision model _(★114, Swift)_
- [system1-agents](https://github.com/ThinkFlowLab/system1-agents) — System 1 decision models (Jev, Laya, Cua-S1) as brain for agents: Browser use, computer use, games and robotics _(★109, Python)_
- [canny](https://github.com/qkal/Canny) — Stops AI coding agents from claiming work is done without evidence. Deterministic hooks decide, TypeSafe's Jev advises. Append-only ledger, zero runtime dependencies. _(★105, TypeScript)_
- [jevgrep](https://github.com/nassim-arifette/jevgrep) — Jev-powered semantic code search for coding agents — find behavior across repositories via CLI or MCP, with exact source excerpts and line numbers. _(★96, TypeScript)_
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) — Connect TypeSafe Jev to Grok Bot as a cheap decision layer - usage gates, skill template, examples _(★92, Python)_
- [jev-desktop](https://github.com/yikangy873-gif/jev-desktop) — TypeSafe Jev action selection inside Codex Computer Use _(★74, JavaScript)_
- [semdecide](https://github.com/sharziki/semdecide) — Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev. _(★72, Python)_
- [ha-jev](https://github.com/AboveColin/HA-Jev) — Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist. _(★69, Python)_
- [jev-recruiter](https://github.com/skeptrunedev/jev-recruiter) — A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence against your hiring brief. _(★49, Python)_
- [jev-sift](https://github.com/kbhuw/jev-sift) — Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification. _(★47, JavaScript)_
- [jev-recall](https://github.com/samdotmak/jev-recall) — Retrieve by relevance, not resemblance: filter an AI assistant's memories with TypeSafe's Jev _(★37, TypeScript)_
- [jevify](https://github.com/altryne/jevify) — An agent skill to discover TypeSafe Jev opportunities, design typed questions, and learn from recent community experiments. _(★35, Python)_
- [pi-advisor](https://github.com/philipbrembeck/pi-advisor) — Fully customizable Advisor and Executor flow plugin for the Pi Coding Agent _(★35, TypeScript)_
- [jev-kit](https://github.com/jonathanavis96/jev-kit) — Everything you need to run TypeSafe's Jev with Claude Code: a tool-call guard, tier guard, file search, browser agent, review, belay, compaction and installers. _(★34, Python)_
- [ai-news-aggregator](https://github.com/flyryan/ai-news-aggregator) — Multi-agent AI news pipeline powered by GLM-5.3-Flash and Jev _(★31, Python)_
- [jev-use](https://github.com/shitianfang/jev-use) — Claude Code / Codex / pi plugin that hands agent steps needing no text output to Jev (TypeSafe's judgment model) — measured p50 ~230 ms and ~$0.02 per 1,000 judgments, with typed escalation back to the LLM _(★27, JavaScript)_
- [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) — Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。 _(★27, Python)_
- [pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) — Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made. _(★26, TypeScript)_
- [jev-harness](https://github.com/TypeSafeAI/jev-harness) — A custom coding harness for TypeSafe AI's Jev: an LLM proposes, Jev answers narrow questions, code decides, every step leaves a receipt. _(★26, TypeScript)_
- [agent-stack](https://github.com/korallis/agent-stack) — Reproducible local multi-agent dev team: OpenRig + Claude Code + Codex + CLIProxyAPI + Jev. Plan in, user-tested features out. _(★25, JavaScript)_
- [jev-doom-agent](https://github.com/lukaske/jev-doom-agent) — A browser-native Doom agent experiment with structured spatial state, composable AI controls, live decision telemetry, and a Chocolate Doom WebAssembly runtime. _(★24, TypeScript)_
- [dsh-jev](https://github.com/buberlo/dsh-jev) — Jev-powered decision layer for DeepSeek Harness _(★24, TypeScript)_
- [jev-native-agent-with-extended-options](https://github.com/6Mikao9/jev-native-agent-with-extended-options) — Research design for a Jev-native agent system:enable more options than jev provided with virtulization and paging, tool integration, external helper logits Top-k proposals with Jev-controlled fallback ,decision-aware hierarchical memory, an _(★23, Python)_
- [jev-axi](https://github.com/shiftynick/jev-axi) — Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell _(★21, TypeScript)_
- [agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) — Screens an AI agent's tool calls before they run and tool results before the agent reads them. An MCP proxy plus a hooks adapter for a client's built-in tools. _(★21, TypeScript)_
- [jcr](https://github.com/NiazMorshed2007/jcr) — A Jev-powered resolver for agent harnesses to find deterministic commands and their context in a nested capability tree. _(★20, JavaScript)_
- [jev-blindspot](https://github.com/jsk4581/jev-blindspot) — A side-panel assistant that finds the blind spots in your prompts. For Claude Code and Codex CLI. _(★20, TypeScript)_
- [jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab) — Real-time drone swarm autonomy simulation using Jev for fast System 1 reflex decisions and collision avoidance, with optional System 2 reasoning for strategic guidance _(★18, TypeScript)_
- [jevbot](https://github.com/lyramakesmusic/jevbot) — discord bot for jev that lets it talk _(★18, Python)_
- [jev-ego](https://github.com/romaluev/jev-ego) — Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move. _(★17, TypeScript)_
- [hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) — TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only. _(★16, Python)_
- *128 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### MCP & Agent Tools (214)

- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. _(★7346, TypeScript)_
- [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) — Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Claude Code and Codex) _(★1002, Python)_
- [distill](https://github.com/samuelfaj/distill) — Get FAR MORE done with FAR FEWER tokens 🔥 _(★691, Rust)_
- [jev-skill](https://github.com/wuyoscar/jev-skill) — An awesome collection of Jev use cases, workflows, and agent skills. _(★560, Python)_
- [jev-mcp](https://github.com/jkudish/jev-mcp) — Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools. _(★484, JavaScript)_
- [perch](https://github.com/lakeday-org/perch) — Semantic code linting with Jev _(★314, JavaScript)_
- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) — An mcp connector to evaluate anything fast and cheap. Give your AI agent direct access to typesafe ai's jev model and open weight models like laya _(★304, Go)_
- [jev-align](https://github.com/sutro-sh/jev-align) — Build calibrated AI Functions from human feedback using Jev and GEPA. _(★302, Python)_
- [skillbox](https://github.com/kitze/skillbox) — Self-hosted, versioned skills library for AI agents. MCP, scoped clients, and optional Jev recommendations. _(★256, TypeScript)_
- [jev-pruner](https://github.com/tamaratran/jev-pruner) — Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it _(★151, TypeScript)_
- [building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — A skill for writing and improving programs that call Jev, TypeSafe's System One model _(★133, n/a)_
- [skillranker](https://github.com/Dicklesworthstone/skillranker) — Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key. _(★127, Rust)_
- [building-with-typesafe-jev](https://github.com/aaddrick/building-with-typesafe-jev) — Unofficial skill that teaches coding agents to build with TypeSafe AI's Jev: typed decisions, calibrated confidence, and prior art from 150+ community projects. _(★127, Python)_
- [jevmem](https://github.com/Avinash-jetwani/jevmem) — Automatic project memory for Claude Code. Also works with Cursor and Codex. _(★105, TypeScript)_
- [formanator](https://github.com/timrogers/formanator) — Submit Forma <https://joinforma.com> benefit claims from the command line and Model Context Protocol (MCP) clients, with support for AI-powered receipt analysis with an LLM or Jev _(★100, Rust)_
- [quicksilver](https://github.com/UditAkhourii/quicksilver) — Claude Code skill: hand bulk judgment calls to Jev. 86% fewer Claude tokens on a 12-task benchmark, up to 20x faster. One-line npx install. _(★98, JavaScript)_
- [dsh-jev-plugin](https://github.com/luobosibing2/dsh-jev-plugin) — Native DeepSeek Harness (DSH) plugin integrating TypeSafe Jev as a System One decision layer for agent selection, supervision, corrections, and approvals. _(★90, JavaScript)_
- [jevintent](https://github.com/Nisaka520/JevIntent) — 微信（FkWeChat 插件）：长按消息分析意图 / 情绪 / 回复姿态，只在本机弹提示，对方无感知 _(★63, Java)_
- [jev-mcp](https://github.com/burnigtm/jev-mcp) — MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client _(★53, TypeScript)_
- [jev-rules](https://github.com/EliaAlberti/jev-rules) — Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter. _(★49, JavaScript)_
- [ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill) — Skill for Hermes, and other agents, to ask typesafe's jev _(★40, Python)_
- [jev-skill-suggester](https://github.com/win4r/jev-skill-suggester) — 用 TypeSafe Jev 推荐已安装 Skill / Bounded installed-skill recommendations with TypeSafe Jev. Python CLI, Codex skill, bilingual docs and live examples. _(★33, Python)_
- [jev](https://github.com/BorisLeMeec/jev) — A claude code plugin for jev _(★33, Go)_
- [pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker) — Rank Pi Agent Skills for the current task with TypeSafe Jev _(★32, TypeScript)_
- [jev-judge-mcp](https://github.com/PyModel/jev-judge-mcp) — Typed judgment tools for MCP agents. TypeSafe's Jev model as verify, screen, find, classify, rerank, decide, compare, extract, review, gate, and score: the model judges, policy decides auto, review, or escalate. _(★29, Python)_
- [jev-cli](https://github.com/shaharia-lab/jev-cli) — Command-line tool for TypeSafe AI's Jev model. Ask yes/no, multiple-choice and rubric questions about any text and get calibrated probabilities back. Answers become exit codes for shells and CI, JSON for scripts, and MCP tools for AI agents _(★27, Rust)_
- [jev-mcp](https://github.com/blakestone-x/jev-mcp) — MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer _(★23, Python)_
- [jev-cli](https://github.com/Nasrallah-AL/jev-cli) — Command-line tool for TypeSafe's Jev AI model _(★22, TypeScript)_
- [jev-linkmap](https://github.com/stas4000/jev-linkmap) — Rebuild a site's internal link map in seconds with Jev, race Claude Opus 5 on the same queue, and let a deep model rewrite the rubric from the disagreements. _(★21, HTML)_
- [claude-jev](https://github.com/0x7067/claude-jev) — Claude Code plugin: Jev for rule checks, verbatim compaction, and prompt routing _(★19, Python)_
- [omo-jev-plugin](https://github.com/brianhong-dev/omo-jev-plugin) — Jev-powered decision support for OmO and senpi agents _(★19, TypeScript)_
- [jevents](https://github.com/JEvents/JEvents) — Main JEvents Repository for core component, modules and plugins _(★19, PHP)_
- [jev-belay](https://github.com/valentynkit/jev-belay) — Claude Code Stop hook that blocks an unverified done: reads the transcript for evidence, asks Jev once, fails open on everything else _(★18, JavaScript)_
- [jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) — Typed, confidence-aware agent skill routing with TypeSafe Jev. _(★18, Python)_
- [jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp) — Hand a whole browser task off in one call: a decision model drives the page server-side, so a flow costs one call, not a turn per click. Ref-based element tables, code-checked assertions, zero-model macro replay, over the Chrome DevTools Pr _(★18, Python)_
- [jevyoumean](https://github.com/syumai/jevyoumean) — Semantic "Did you mean?" for any CLI — wraps commands and uses TypeSafe's Jev to match subcommand typos by intent, not edit distance. _(★16, Go)_
- [jev-studio](https://github.com/utk2103/jev-studio) — if you're experimenting with jev it will be easier from here _(★16, Python)_
- [atoma](https://github.com/mgtf/atoma) — Watch a request turn into finished work. AI agents produce and check it; TypeSafe's Jev decides. _(★16, TypeScript)_
- [jev-cli](https://github.com/tumf/jev-cli) — Small dependency-free CLI for TypeSafe Jev _(★14, Python)_
- [typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router) — TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn. _(★14, Python)_
- [beam-cli](https://github.com/whyashthakker/beam-cli) — Monitoring & Safety layer for all your agents. Open Source CLI & Skills for Claude Code, Codex, Cursor, Jev and your preferred agents. _(★12, TypeScript)_
- [dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) — Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate completion claims inside DeepSeek Harness. _(★11, TypeScript)_
- [jev-permission-gate](https://github.com/madisonrickert/jev-permission-gate) — A Claude Code mod that uses TypeSafe's Jev to decide auto mode tool calls. 2x faster than the built-in classifier on the calls it decides. _(★10, TypeScript)_
- [jev-mcp](https://github.com/rashedInt32/jev-mcp) — MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin. _(★8, TypeScript)_
- [jev-mcp](https://github.com/arunav25/jev-mcp) — Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy. _(★8, JavaScript)_
- [dsh-jev-plugin](https://github.com/jackie-cqz/dsh-jev-plugin) — DeepSeek Harness plugin for TypeSafe Jev: typed decisions, configurable guardrails, and Web UI result cards. _(★8, TypeScript)_
- [jev.nvim](https://github.com/valentynkit/jev.nvim) — Neovim: ask the buffer a question, get a quickfix list. Treesitter splits functions, Jev scores each one, probabilities land as virtual text _(★7, Lua)_
- [jev-skill-router](https://github.com/shimo4228/jev-skill-router) — Claude Code plugin: asks TypeSafe Jev which installed skill fits each prompt and logs the answer (shadow-first). A working reference for the skill-suggestion cookbook on Claude Code — the README records why it is unlikely to help a strong m _(★7, Python)_
- [jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate) — Cut Claude Code's skill manifest by ~75% with TypeSafe Jev. Scores every installed skill for relevance and hides the rest via skillOverrides — 12,750 → 3,185 tokens on a 217-skill install, for $0.0009 a session. _(★7, JavaScript)_
- [jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) — Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark. _(★6, Python)_
- *164 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Web & Browsing (103)

- [jevgrep](https://github.com/dzhng/jevgrep) — Find code by asking what it does. A CLI for coding agents that uses Jev to discover relevant files and source context. _(★2094, TypeScript)_
- [jev-browser-use](https://github.com/wy-coliney/jev-browser-use) — 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp. _(★819, JavaScript)_
- [jev-search](https://github.com/superagents-lab/jev-search) — Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API. _(★507, TypeScript)_
- [jev-seo](https://github.com/AgriciDaniel/jev-seo) — Live SEO audit for any website from one homepage URL, judged by Jev. PDF, XLSX and Markdown reports. _(★484, Python)_
- [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) — Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence. _(★382, JavaScript)_
- [unclutter](https://github.com/kitze/unclutter) — WXT browser extension: Jev-powered page clutter removal with reusable template rules. _(★348, TypeScript)_
- [jev-browser](https://github.com/jkudish/jev-browser) — Browser use using Typesafe's Jev model _(★306, JavaScript)_
- [jev-browser](https://github.com/openqa-cn/jev-browser) — Jev Browser — indexed browser automation. Jev chooses the control, Playwright acts. A CodexQA skill. _(★105, TypeScript)_
- [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) — A fast browser agent: Jev picks each action from what is on the page, an LLM reads and plans, and every claim in an answer cites a quote from the page. _(★102, Python)_
- [jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) — Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server. _(★94, JavaScript)_
- [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) — jev-seo: Rust SEO and GEO CLI plus MCP server for coding agents: 50-rule audits, live crawls, GEO scores, rank drift, CI gates. MIT, zero subscription. _(★94, Rust)_
- [blink](https://github.com/ellipsis-dev/blink) — Codebase search powered by Jev from @typesafe-ai _(★78, TypeScript)_
- [RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev) — Typed-decision models (noul / choice / score) trained by a self-improving loop of AI agents — checkpoints, the code that produced them, and every version that failed. _(★45, Python)_
- [jgrep](https://github.com/kyu1204/jgrep) — grep for what code does, not what it's called. Semantic code search powered by TypeSafe Jev. _(★34, TypeScript)_
- [jev-on-a-laptop](https://github.com/rorshopping/jev-on-a-laptop) — Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo. _(★25, Python)_
- [slop-filter](https://github.com/adamnroman/slop-filter) — Chrome extension that hides AI-generated posts and comments on X, LinkedIn, and Reddit. Scored by TypeSafe Jev. _(★22, JavaScript)_
- [zero-api-key-web-search](https://github.com/wd041216-bit/zero-api-key-web-search) — Jev-powered search infrastructure for AI agents: zero API keys, MCP-ready, LLM-context aware, with local neural evidence verification. _(★18, Python)_
- [lkclean](https://github.com/stefw/lkclean) — Chrome extension that cleans up your LinkedIn feed: hides engagement bait, self-promo and off-topic posts using Jev, TypeSafe AI's typed classification model — and explains every decision. _(★16, TypeScript)_
- [laya-browser-agent](https://github.com/ChenneyZhuang/laya-browser-agent) — Local, open-source Jev alternative: browser agent decisions with Laya (System One model) on your own machine. No cloud, no API key. Playwright/CDP, MCP-friendly. _(★16, Python)_
- [jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed) — BRRRRRRRRRRRRRRRRRRRRRR _(★12, Python)_
- [jev-agent-browser](https://github.com/forvela/jev-agent-browser) — Fast, bounded browser agents powered by Jev and agent-browser — typed actions, research, classification, and safe orchestration. _(★11, JavaScript)_
- [jev-browser](https://github.com/tontoko/jev-browser) — One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions. _(★10, JavaScript)_
- [jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) — Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured. _(★9, Python)_
- [jev-browser-bridge](https://github.com/lexmount/jev-browser-bridge) — Plug any CDP browser into Jev — cloud, local or self-hosted, including browsers that never draw a page. _(★9, Python)_
- [hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) — Autonomous multi-source rental search powered by TypeSafe Jev _(★9, JavaScript)_
- [jevsearch](https://github.com/kylemclaren/jevsearch) — Site search that understands the question. Ranked by TypeSafe's Jev model. _(★6, TypeScript)_
- [pagegrade](https://github.com/kitze/pagegrade) — Grade page sections for clarity, writing and on-page SEO. WXT + TypeSafe AI Jev. _(★6, TypeScript)_
- [jev-search](https://github.com/larguesa/jev-search) — Experimental semantic line search with TypeSafe Jev via OpenRouter. Python CLI with no runtime dependencies. _(★6, Python)_
- [jev-frontend-qa](https://github.com/Nainish-Rai/jev-frontend-qa) — Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo. _(★5, Python)_
- [jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh) — Jev 模型（TypeSafe AI）官方使用文档的中文翻译 | Unofficial Chinese translation of the official Jev (TypeSafe AI) docs — https://docs.typesafe.ai _(★5, Jupyter Notebook)_
- [jev-browser-control](https://github.com/nexibeo/jev-browser-control) — Let Claude code, chatgpt codex or control your own Chrome. Chrome extension + MCP server: Jev, TypeSafe's decision model, picks each click in ~0.5 s for a fraction of a cent. MIT, bring your own OpenRouter key. _(★5, JavaScript)_
- [jev-trip](https://github.com/liaoyuhua/jev-trip) — Two Minds, One Trip.  https://jev-trip.vercel.app/ _(★4, TypeScript)_
- [tinycomputer](https://github.com/tinyhumansai/tinycomputer) — Decision model (JEV) based harness to perform Desktop & Browser automation. Written in Rust.  _(★4, Rust)_
- [jev-research-eval](https://github.com/jgridifier/jev-research-eval) — Reproducible Jev Ultrafast research-browser eval harness + field note (QC’d cases, suite runner, report generator). Not investment advice. _(★3, HTML)_
- [tsai-civ2](https://github.com/phyous/tsai-civ2) — TypeSafe Jev plays original Civilization II in a browser, with live action probabilities. Experimental full-game harness. _(★3, Python)_
- [jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot) — A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification. _(★3, Python)_
- [jev-turbo](https://github.com/sightmap/jev-turbo) — Jev-powered semantic browser use _(★3, Go)_
- [jev-2048-selenium](https://github.com/AMMIROSOH/jev-2048-selenium) — Selenium 2048 player powered by expectimax search and TypeSafe Jev, with portrait FFmpeg recording. _(★3, Python)_
- [auto-mode-for-paseo](https://github.com/obetomuniz/auto-mode-for-paseo) — Paseo plugin that routes each message to a persona on Codex, Claude, OpenCode, or any other installed provider. _(★3, TypeScript)_
- [what-the-jev](https://github.com/keta1930/what-the-jev) — What can Jev actually do? Reproducible experiments and research reports exploring its capabilities and limits. _(★3, Python)_
- [jev-reranker](https://github.com/shinpr/jev-reranker) — Rerank, filter, and compress JSON search results with TypeSafe AI's Jev. _(★2, Rust)_
- [jev-resilience](https://github.com/Vicente-MD/jev-resilience) — Non-blocking Spring Boot Starter for Spring WebFlux that implements a Semantic Circuit Breaker to detect silent HTTP 200 failures using TypeSafe Jev. _(★2, Java)_
- [psearch](https://github.com/komikat/psearch) — Parallel web search for terminals and agents, with local Chromium and Jev-guided exploration. _(★2, Python)_
- [decido](https://github.com/yairshy/decido) — Probabilistic decisions for Python. Use Jev or bring your own provider; crawl with Playwright. _(★2, Python)_
- [paper-package](https://github.com/CompleteDotTech/paper-package) — Jev research manuscript, evidence, and reproducible paper package _(★2, Python)_
- [ajevt-browser](https://github.com/XYenon/ajevt-browser) — A bounded Jev System-1 browser tool for Pi, OpenCode V2, Amp, and MCP, powered by agent-browser _(★2, TypeScript)_
- [JEV](https://github.com/Chorylee7/JEV) — JEV 调研报告：TypeSafe System One 决策模型与开源对标（含原始核实记录） _(★2, Python)_
- [semble-jev](https://github.com/fatelei/semble-jev) — A code search CLI for coding agents. Semble retrieves source snippets locally, Jev evaluates their relevance, and the CLI returns selected original source with locations for further reading. _(★2, Python)_
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) — Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev: passes six pre-registered gates on 360 labeled rows, fails four of six on graded product  _(★1, Python)_
- [jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline) — Daily research monitor for standing questions: deterministic Python owns the loop, TypeSafe Jev screens sources per question, Qwen writes the notes (pilot) _(★1, Python)_
- *53 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Developer Tools (145)

- [pg-jev](https://github.com/realZachi/pg-jev) — Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev. _(★402, Shell)_
- [astra-ares](https://github.com/miuuyy/Astra-Ares) — Adaptive reasoning effort for GPT-6 during Codex tasks, powered by Jev to reduce token usage. _(★295, JavaScript)_
- [jeff](https://github.com/logan-markewich/jeff) — A self-hosted drop-in replacement for TypeSafe's jev, powered by GliFormer. _(★284, Python)_
- [jeva](https://github.com/jevajs/Jeva) — A monorepo for code used in videos/tutorials for Jeva. Created and maintained by @thatziv _(★226, Lua)_
- [stanley-code](https://github.com/devagrawal09/stanley-code) — Bounded TypeSafe Jev workflows for coding agents. _(★115, TypeScript)_
- [jev-lint](https://github.com/mizchi/jev-lint) — lint text in code by jev scorerer _(★115, TypeScript)_
- [jegrep](https://github.com/can1357/jegrep) — Semantic grep: find code by describing what you're looking for, powered by Jev. _(★90, Rust)_
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) — Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification _(★85, C)_
- [jev-libero](https://github.com/Dimweaker/jev-libero) — Fine-grained robot control with Jev, physics previews, and configurable LIBERO tasks. _(★80, Python)_
- [djev](https://github.com/mmastrac/djev) — Jev-style structured decisions on DiffusionGemma: the example server from vLLM PR 57250 _(★80, Python)_
- [typesafe-adblock](https://github.com/realZachi/typesafe-adblock) — 🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker. _(★75, JavaScript)_
- [social-monitor](https://github.com/777genius/social-monitor) — Tired of scrolling through hundreds of near-identical posts across every social network just to find the few that actually matter. Instead of drowning in duplicate takes, reposts, and filler from X, Reddit, news sites, I wanted one tool tha _(★48, TypeScript)_
- [commit-miner](https://github.com/devanshbatham/commit-miner) — Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types. _(★36, Rust)_
- [snifftest](https://github.com/DanRWilloughby/snifftest) — A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model. _(★31, TypeScript)_
- [jev-code](https://github.com/FrancoisChastel/jev-code) — Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and OpenCode: typed classify, check, score, rank, and ask, plus one-command setup. _(★31, TypeScript)_
- [is-malicious](https://github.com/luantak/is-malicious) — A codebase scanner that helps you not run malicous code _(★26, TypeScript)_
- [jev-design-test](https://github.com/bhaiG-de/jev-design-test) — Jev shadcn-block generator _(★26, TypeScript)_
- [duckdb-jev](https://github.com/colliber/duckdb-jev) — DuckDB extension: typed Jev answers as real SQL types _(★25, C++)_
- [jev-column-race](https://github.com/goodrahstar/jev-column-race) — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper _(★24, JavaScript)_
- [jev-ui-test](https://github.com/buer2233/jev-ui-test) — Jev 决策模型驱动的 UI 自动化测试框架：不生成「下一步做什么」的文字，而是在候选元素里直接打分；一句话写用例，pytest 执行，Allure 出报告，每个操作决策中位 458 ms（UI test automation driven by the Jev decision model — scored decisions, not generated prose; ~458 ms per decision） _(★23, Python)_
- [jev-agent-design-with-topk-logits-choices](https://github.com/6Mikao9/jev-agent-design-with-topk-logits-choices) — Research design for a Jev-native agent system: tool integration, speculative parameter proposals, external helper logits Top-k proposals with Jev-controlled fallback ,decision-aware hierarchical memory, and dependency-aware replanning.Featu _(★22, Python)_
- [erislint](https://github.com/Eriskii/ErisLint) — Rust linter powered by configurable Jev rules, with a VS Code extension. _(★20, Rust)_
- [jev-code](https://github.com/rhighs/jev-code) — Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation. _(★20, TypeScript)_
- [jev-test-filter](https://github.com/mizchi/jev-test-filter) — Score every test against a git diff with Jev, and emit the filter arguments vitest, node:test, Playwright, cargo test and go test already understand _(★19, TypeScript)_
- [jevonian](https://github.com/xinyao27/jevonian) — One local endpoint. The right model for every turn — enforced in code, not prompts. _(★15, TypeScript)_
- [jevbetter](https://github.com/olanotolu/jevbetter) — A stronger one-pass scorer over a variable list of text options. Hashed n-gram encoder, rival-aware attention, gated head, temperature scaling — with a head-to-head benchmark vs the jevlike starter design. _(★15, Python)_
- [jev-commit](https://github.com/valentynkit/jev-commit) — pre-commit hook: one Jev call judges whether your commit message matches the diff, plus debug leftovers, scope creep, and a secret belt _(★13, Python)_
- [jevql](https://github.com/kylemclaren/jevql) — Semantic SQL for Postgres, powered by Jev _(★13, Go)_
- [lintus](https://github.com/virolea/lintus) — A linter whose rules are written in plain language. _(★13, Rust)_
- [duomind](https://github.com/j1s4nn/duomind) — Pair a small local LLM (System 2) with a fast classification API (System 1) to make 3B models reason like bigger ones — OpenAI-compatible, private, and almost free to run. _(★13, Python)_
- [jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm) — Zero-shot English goals on a sim Franka. Jev chains hardcoded primitives. _(★12, Python)_
- [jevlint](https://github.com/iamtoomas/JevLint) — Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin. _(★12, TypeScript)_
- [jevsdsql](https://github.com/Sheltercosmo/JevSDSQL) — A self-developing SQL database with JEV based semantic operators and natural language queries. _(★12, Python)_
- [jevpr](https://github.com/HexyeDEV/JevPR) — PR Risk review, automated by Jev _(★9, Python)_
- [every](https://github.com/sufianetaouil/every) — Ask a yes/no question of every function in a codebase. Ranked answers in seconds, for cents. Grep whose pattern is a question, powered by TypeSafe Jev. _(★8, Python)_
- [codex-sift](https://github.com/romanmeclazcke/codex-sift) — Route each Codex turn to the cheapest model that can handle it, judged by TypeSafe Jev. _(★8, TypeScript)_
- [taste-lint](https://github.com/mblode/taste-lint) — Catch AI slop before you ship. _(★7, TypeScript)_
- [jevtest](https://github.com/joshhu/jevtest) — 情緒測謊器：嘴上說「好」，心裡真的好嗎？用 TypeSafe Jev（System One 模型）透過 OpenRouter 即時判斷，並與一般 LLM 對照 _(★7, HTML)_
- [duckdb-jev](https://github.com/prasanthj/duckdb-jev) — High-throughput, robust native DuckDB extension for batched and streaming TypeSafe/Jev classification, scoring, and semantic predicates from SQL. _(★6, C++)_
- [jevsql](https://github.com/EugeneBoondock/jevsql) — SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by meaning — batched, cached and cost-guarded. _(★6, JavaScript)_
- [riff](https://github.com/scale-venture-partners/riff) — A small, fast prose linter: ruff-style rule codes for writing, backed by TypeSafe's Jev model _(★6, Python)_
- [jev-codex-bridge](https://github.com/ansidium/jev-codex-bridge) — Model and reasoning routing for Codex Desktop and CLI, with a Windows service and validated updates _(★6, JavaScript)_
- [datafusion-jev](https://github.com/hotdata-dev/datafusion-jev) — Typed Jev decisions in DataFusion SQL _(★6, Rust)_
- [jev-codex-token-saver](https://github.com/jcressler/jev-codex-token-saver) — Experimental Jev evidence selection for token-efficient Codex investigations _(★6, JavaScript)_
- [fast-jev-opencode](https://github.com/nrdz-labs/fast-jev-opencode) — Jev-scored context pruning for OpenCode: drops stale tool calls and truncates bulky results on the outgoing request — fail-open, cache-backed, configurable live. Port of fast-jev-compaction to the V2 context hook. _(★6, TypeScript)_
- [jev-rag](https://github.com/aifabrice/jev-rag) — Vector-free local RAG with SQLite BM25, Jev reranking, and grounded LLM answers. No embeddings or vector database. _(★6, Python)_
- [jev-skip](https://github.com/valentynkit/jev-skip) — YouTube sponsor skipper that reads the captions and decides at watch time: a probability heatmap on the seek bar, no crowd database _(★5, TypeScript)_
- [mysql-ailike](https://github.com/maayanlevy/mysql-ailike) — Natural-language row filtering for MySQL, powered by TypeSafe Jev. _(★5, C++)_
- [jev-action](https://github.com/cachix/jev-action) — Run Jev judgments in GitHub Actions, including pull request label triage _(★5, TypeScript)_
- [jev-claude-code](https://github.com/DarioFontanel/jev-claude-code) — Prompt Claude Code: tre sistemi costruiti su Jev di TypeSafe — routing del modello, compattazione del contesto e code review _(★5, n/a)_
- *95 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Games & Play (125)

- [minecraft-agent](https://github.com/rmalde/minecraft-agent) — Astra planner and JEV controller for Minecraft, with native recording, tested routes, and run verification. _(★572, JavaScript)_
- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) — A TypeSafe/Jev agent that plays Super Mario Bros. from structured emulator state. _(★426, Python)_
- [jeveassets](https://github.com/GoldenGnu/jeveassets) — jEveAssets is an out-of-game asset manager for Eve-Online, written in Java _(★196, Java)_
- [advocaat](https://github.com/pithings/advocaat) — A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev. _(★92, TypeScript)_
- [jev-pokemon](https://github.com/christianmat/jev-pokemon) —  _(★67, TypeScript)_
- [jevify](https://github.com/fidecastro/jevify) — Supersimple way to serve LLMs as a Jev-like endpoint _(★47, Python)_
- [pi-typesafe](https://github.com/DevMortimer/pi-typesafe) — TypeSafe decisions for Pi: batched evaluation tool, terminal playground, and typed API for extension authors _(★46, TypeScript)_
- [jev-spring-boot-starter](https://github.com/danvega/jev-spring-boot-starter) — A simple Spring Boot 4 starter for TypeSafe Jev using Spring MVC and RestClient _(★37, Java)_
- [jevtown](https://github.com/NevaMind-AI/JevTown) — jev based AI town simulation _(★36, TypeScript)_
- [playjev](https://github.com/OmniJev/PlayJev) — 🚀🚀 A 0.8B JEV-like multimodal model playing GUI games directly from raw pixels. _(★34, JavaScript)_
- [tsai-sc](https://github.com/phyous/tsai-sc) — TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities. _(★26, Python)_
- [typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground) — Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI. _(★21, TypeScript)_
- [jpp](https://github.com/Towow-ai/jpp) — J++: an experimental language with standalone source and a Rust runtime. Compose questions and methods. 独立源码，组合问题与方法。 _(★19, Rust)_
- [jevframe](https://github.com/ktaletsk/jevframe) — Semantic AI for pandas and Polars: classify text, analyze sentiment, and score DataFrame rows with natural-language questions and full probabilities using TypeSafe Jev. _(★18, Python)_
- [jevil-simulator](https://github.com/KRLW890/jevil-simulator) — A simulator for the Jevil bossfight in Deltarune. _(★18, JavaScript)_
- [muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook) — Jev decision layer for Muse: a fast, cheap TypeSafe AI gate before expensive agent work — confidence policy, recipes, reference router, honest measurement. _(★17, Python)_
- [jev-tetris](https://github.com/trungdq88/jev-tetris) — Jev play Tetris in real-time against other AI models _(★15, JavaScript)_
- [typesafe-playground](https://github.com/kavehmz/typesafe-playground) — Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs. _(★14, JavaScript)_
- [omnijev](https://github.com/shapsider/OmniJev) — OmniJev — multimodal finite-choice decision interface and MuJoCo embodied workbench: trajectory replays, decision probes, benchmark panels, 60s walkthrough. _(★13, Python)_
- [jevpokerbench](https://github.com/Prophetlab/JevPokerBench) — ProphetLab's Texas Hold'em benchmark and playground for decision models: cash and SNG leaderboards, live replays, and bring-your-own-agent tables. _(★11, Python)_
- [playjev](https://github.com/filedcom/playjev) — Fast, typed browser automation powered by Jev and Playwright _(★10, TypeScript)_
- [typesafe-local](https://github.com/aabolfazl/typesafe-local) — Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon. _(★9, Python)_
- [typesafe-chess](https://github.com/TholeG/typesafe-chess) — Chess where both players are TypeSafe's Jev model: every move is a typed Choice decision _(★8, JavaScript)_
- [jev-sim-use](https://github.com/Ryu0118/jev-sim-use) — 📱 Reach any screen with sim-use at Jev speed _(★8, Swift)_
- [hermes-and-jev-play-minecraft](https://github.com/teknium1/hermes-and-jev-play-minecraft) — Hermes Agent plans, Jev (TypeSafe) picks bounded actions, Mineflayer executes: Minecraft with no screenshots or keypresses from a model. Includes the reproduction of rmalde/minecraft-agent's Ender Dragon run. _(★8, JavaScript)_
- [usejev](https://github.com/ali-master/usejev) — Run Laya locally with Bun: native ONNX inference, a TypeSafe-compatible API, and a bilingual decision playground. _(★8, TypeScript)_
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) — Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks at branches in about 100 ms, calibration measured instead of assumed _(★7, Python)_
- [jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner) — Chrome dino game played by Typesafe AI Jev model _(★7, JavaScript)_
- [jev-grand-prix](https://github.com/enoyola/jev-grand-prix) — An F1 racing game where TypeSafe's Jev picks the racing line and the pedals, and learns each corner's limit between laps _(★7, JavaScript)_
- [jev-clerk](https://github.com/stas4000/jev-clerk) — A desktop bookkeeping clerk: Jev decides every step, Fable 5.1 rewrites its playbook every ten invoices _(★7, Python)_
- [jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) — Playing Pokemon Red using TypeSafe Jev _(★6, Python)_
- [typesafe-ai-playground](https://github.com/markjaquith/typesafe-ai-playground) — A playground for experiments around Jev, TypeSafe's System One model. _(★5, Rust)_
- [jevchess](https://github.com/choxos/jevchess) — Jev, TypeSafe's System One model, plays chess against any OpenRouter LLM, Stockfish and you. One-page web app with live moves, Jev's move probabilities, saved games and win rates. _(★5, JavaScript)_
- [jevplayspokemon](https://github.com/anxkhn/JevPlaysPokemon) — Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM. _(★5, HTML)_
- [jev-helper](https://github.com/ra2web/jev-helper) — A helper which use JEV to play ra2web(WannaFire Version)[王二火大] _(★5, JavaScript)_
- [jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) — Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation. _(★4, JavaScript)_
- [typesafe-ai-playground](https://github.com/nickthompson480/typesafe-ai-playground) — Community TypeSafe AI playground: 110 use cases, games, dilemmas and model challenges, with editable prompts, A/B comparisons and a mobile-friendly UI. _(★4, JavaScript)_
- [snake-jev](https://github.com/siroccomask/snake-jev) — Snake controlled by parallel Jev assessments, with one API call per game tick. _(★3, Python)_
- [jev-play-ping-pong](https://github.com/Icohen007/jev-play-ping-pong) — Jev plays browser table tennis in real time: structured telemetry, typed decisions, ordinary Chrome inputs, and auditable evidence. _(★3, JavaScript)_
- [got-jev](https://github.com/phureewat29/jev-got) — Jev (TypeSafe AI) PoC through Game of Thrones _(★3, TypeScript)_
- [typesafe-arena](https://github.com/DeepBlueDynamics/typesafe-arena) — A playground for TypeSafeAI's Jev Model _(★3, Rust)_
- [jev-plays](https://github.com/mansicer/jev-plays) — A System One model (jev) plays Craftax; an LLM sets the goals _(★3, Python)_
- [system-one-chess](https://github.com/dperezcabrera/system-one-chess) — Chess against Jev, TypeSafe AI's System One model, through OpenRouter. Built with the pico framework. _(★3, Python)_
- [ask-jev-ai](https://github.com/waynesutton/ask-jev-ai) — A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answers yes, no, or it depends in about 100 milliseconds. Every judged ask lands on the wall in realtime, with a running count toward o _(★3, JavaScript)_
- [sedum](https://github.com/sedum-dev/sedum) — Plain-English browser e2e tests cheap enough to run on every PR. Built on Jev and Playwright, open source, bring your own key. _(★3, TypeScript)_
- [jevcraft](https://github.com/mrubens/jevcraft) — Jev-powered Minecraft bot _(★3, JavaScript)_
- [jev-nethack](https://github.com/statico/jev-nethack) — TypeSafe's Jev model plays NetHack 5.0: code lists the legal moves, Jev picks one, no LLM in the loop _(★3, Python)_
- [hunch](https://github.com/steven-shoemaker/hunch) — Ask Jev over columns of data: closed-set questions, cached and joined back. _(★2, Python)_
- [jev-playground](https://github.com/Little-Planet-Labs/jev-playground) — A small Next.js app for experimenting with TypeSafe AI's Jev model (System One) _(★2, TypeScript)_
- [jev-playground](https://github.com/wustep/jev-playground) — Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI. _(★2, TypeScript)_
- *75 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Chat & Messaging (66)

- [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) — 装在手机上的对话副驾：在 QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。 _(★7282, Kotlin)_
- [jev-chat-windows](https://github.com/jev-chat/jev-chat-windows) — JevChat-Windows：聊天窗口旁挂的回复辅助。窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动 _(★727, Python)_
- [jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac) — 聊天悬浮窗助手（macOS）：屏幕感知 + 本地小模型判断意图与风险，按话术生成回复候选。纯只读。 _(★453, Python)_
- [goutoujunshi-jev-chat](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat) — 狗头军师 Chat：Mac 微信读屏、关系分析与回复草稿悬浮窗 _(★271, Python)_
- [332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat) — Jev Chat Assistant for Windows - 电脑版微信意图判断与 DeepSeek 建议回复 _(★163, Kotlin)_
- [jev-chat](https://github.com/w3cj/jev-chat) — A tool calling chat bot built with Jev and no LLM. _(★108, TypeScript)_
- [jevchat](https://github.com/kyle-pena-nlp/jevchat) — Turns Jev into a chatbot _(★91, Python)_
- [jev](https://github.com/dannote/jev) — TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer _(★35, Elixir)_
- [st-jeved](https://github.com/mossyfield/ST-jeved) — SillyTavern extension that measures each reply and instructs the narrator only when a rule matches. _(★31, JavaScript)_
- [jev-yaba-wechat](https://github.com/wuxie888/jev-yaba-wechat) — 微信里的话不知道怎么接？macOS 悬浮聊天助手：识别消息意图与沟通风险，GPT 生成多种话术，Jev 评估候选，一键填入微信。话我帮你想，发送你来定。 _(★22, Python)_
- [jev-chat-jarvis-ios](https://github.com/jev-chat/jev-chat-jarvis-ios) — iPhone 键盘版：一个自定义键盘打通所有聊天 App——长按复制对方消息，键盘上出意图、风险与候选回复，点一下进输入框。只读剪贴板，源码形式（需自行用 Xcode 编译安装）。 _(★15, Swift)_
- [wechat-jev-assistant](https://github.com/yushen100/wechat-jev-assistant) — Windows 微信对话分析助手：本地读取、脱敏、TypeSafe Jev 判断与加密历史 _(★14, Python)_
- [jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch) — Filter any live Twitch chat with Jev: a bring-your-own-key Chrome extension _(★13, JavaScript)_
- [sift](https://github.com/bohutang/sift) — Chrome extension that labels every post on X (Substance · Humor · Chit-chat · Promo · Junk · AI-written) with TypeSafe Jev, and hides the ones you don't want. _(★12, JavaScript)_
- [jevbystander](https://github.com/Nisaka520/JevBystander) — 安卓无障碍版微信判读：只读屏、只弹 3 条 Toast（意图 / 情绪 / 着急 / 建议），不生成回复文案、不发送 · 零第三方依赖，APK 861 KB _(★10, Kotlin)_
- [jevguide](https://github.com/Nisaka520/JevGuide) — 弦外之音 —— 微信聊天里的关系进展助手：读屏（无障碍树 / 截屏视觉）→ Jev 判读 + 攻略度 → 聊天模型出 3 条候选回复，攻略度常驻挂在屏幕上。不改微信、不发消息、不注入点击。 _(★10, Kotlin)_
- [jev-chat-windows](https://github.com/caizili999/jev-chat-windows) — Windows 微信回复助手（非官方修改版）：本地离线 OCR 读屏 + 模型起草候选回复 + 一键填入微信输入框，可选自动发送。不 hook、不注入、不读微信数据库。 _(★8, Python)_
- [xscout-jev](https://github.com/ethan-ab/xscout-jev) — Watch X for the news that matters to you, judged by Jev, and get alerted in Slack. Set up by an AI agent. _(★8, TypeScript)_
- [jev-bigquery-cloudrun](https://github.com/jeffonelson/jev-bigquery-cloudrun) — Classify support tickets in BigQuery with Jev and Cloud Run _(★7, Python)_
- [jev-chat-windows-deepseek-jev](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev) — DeepSeek + TypeSafe JEV 微信回复助手：Windows 正式版、Apple Silicon macOS 预览版；本地 OCR 与人工可控回复 _(★6, Python)_
- [jev-chat](https://github.com/adhyaay-karnwal/jev-chat) — A chatbot from typed Jev decisions: hierarchical speculative decoding over System One probabilities. _(★5, Python)_
- [pi-jev-compaction](https://github.com/nourhelmi/pi-jev-compaction) — Automatic Jev context clearing for Pi. Keep the conversation, prune stale tool output, retrieve originals without rerunning commands. _(★4, TypeScript)_
- [chat2jev](https://github.com/Chandler-Sun/chat2jev) — Convert legacy chat completion API request to Typesafe jev API _(★3, TypeScript)_
- [jev-freeform](https://github.com/kesku/jev-freeform) — An observable raw-character chat experiment powered entirely by TypeSafe Jev Choice _(★3, JavaScript)_
- [jev-chat-gate](https://github.com/pandore/jev-chat-gate) — A framework-independent participation gate for AI agents in group chats, powered by typed Jev decisions. _(★3, JavaScript)_
- [lanebreak](https://github.com/ndolinschi/lanebreak) — LaneBreak — support ticket priority+routing via TypeSafe Jev _(★1, TypeScript)_
- [scam-shield](https://github.com/ShupingR/scam-shield) — Scam text message filter powered by TypeSafe's Jev model _(★1, TypeScript)_
- [jev-inbox-queue](https://github.com/tusharck/jev-inbox-queue) — Turn an inbox into a short action queue with Jev (TypeSafe System One) _(★1, Python)_
- [guardrail-chatbot-jev](https://github.com/taman-spirit/guardrail-chatbot-jev) — Vietnam - Content safety guardrails for AI chatbots: input, output and conversation checks over one policy file with Jev _(★1, Python)_
- [mailroom](https://github.com/Kevin-Liu-01/mailroom) — Your Gmail, sorted. Rules you can read, typed AI judgments from TypeSafe's Jev for pennies, receipts and undo for everything. _(★1, TypeScript)_
- [jevmod](https://github.com/ohernandezdev/jevmod) — Moderation for communities and apps, powered by Jev (TypeSafe): probabilities per category, thresholds you own. Discord/Telegram/Reddit bots, CLI, Python, npm, HTTP API, MCP. _(★1, Python)_
- [Codex_ChatGPT_JEV_Switch](https://github.com/FlyPig23/Codex_ChatGPT_JEV_Switch) — Fork of codex-with-chatgpt: TypeSafe Jev + deterministic rules decide when Codex hands work to ChatGPT web (plan, debug, review) and when it switches back. 用 Jev 自动决定 Codex 与网页版 ChatGPT 何时切换。 _(★1, TypeScript)_
- [sortroom](https://github.com/mhoenes/sortroom) — Self-hosted IMAP mail sorter: a classification model (any TypeSafe API service, e.g. Jev) files new mail into your folders, stars what needs action and tracks expiring offers. Docker image with a web admin UI. _(★1, Python)_
- [crush-monitor-universal](https://github.com/Reverie0123/crush-monitor-universal) — Crush 好感监控器 通用版 · Crush Monitor (Universal): read the feelings in your chats with the original Jev or DeepSeek / OpenAI. 中文 / English. Adapted from FerryCorleone's original, with permission. _(★1, TypeScript)_
- [jev-chat-jarvis](https://github.com/SanHsien/jev-chat-jarvis) — 裝在手機上的「對話副駕」：讀取最新訊息、AI 分析意圖並建議回覆，一鍵填入聊天輸入框。｜A conversation co-pilot on your phone: analyzes incoming messages, suggests replies, and fills them into chat apps. _(★1, Python)_
- [tidy](https://github.com/abhibansal60/tidy) — Clean up Gmail and YouTube with AI, safely: Jev judges each email or channel, plain code sets the limits, you approve. pipx install tidy-ai _(★1, Python)_
- [last-lst97-dev](https://github.com/lst97-oss/last-lst97-dev) — Simple personal profolio plus chat assistance with RAG and Jev 🇦🇺🇭🇰 _(★0, TypeScript)_
- [chat-jev-mac](https://github.com/buildforpeople4iv/chat-jev-mac) — 聊天消息意图与风险识别助手：macOS 悬浮窗（微信）+ Chrome 扩展（网页端聊天）。纯只读，不注入、不自动发送。 _(★0, Python)_
- [astrbot_plugin_jev_active_reply](https://github.com/muyouzhi6/astrbot_plugin_jev_active_reply) — Jev主动回复插件 · 作者木有知 · TypeSafe/MindsHub多Key与同人连续补充合并 _(★0, Python)_
- [jev-ai-emails-flow](https://github.com/tarunchandel/jev-ai-emails-flow) — AI-powered email flow automation _(★0, Python)_
- [jevgraph](https://github.com/murabcd/jevgraph) — Visual chatflows with Jev, OpenAI, Gemini, and Convex. _(★0, TypeScript)_
- [mynameisjev](https://github.com/bradsec/mynameisjev) — Jev model router plugin for Claude Code: routes each message to the cheapest fitting Claude model or Codex _(★0, JavaScript)_
- [sieve](https://github.com/gdamiani1/sieve) — Sieve: a Chrome extension that scores which LinkedIn and Reddit posts are worth your time and suggests reply angles, built on TypeSafe's Jev. Never posts for you. _(★0, JavaScript)_
- [email-triage-benchmark](https://github.com/frankstu/email-triage-benchmark) — Benchmark: JEV vs. LLMs (Claude Haiku, GPT-6 Luna) für E-Mail-Triage – Qualität, Latenz, Kosten. Mit lokaler Pseudonymisierung. _(★0, Python)_
- [jevchik](https://github.com/smixs/jevchik) — Telegram bot for group chats: karma for useful messages, anti-spam for newcomers, a Mini App leaderboard. Judged by the Jev model. _(★0, TypeScript)_
- [JevJarvis-liuhai-IOS](https://github.com/haha145142/JevJarvis-liuhai-IOS) — Jev Jarvis iOS 终极融合版 v1.5（含键盘扩展、内置知识库、多消息上下文；云编译未签名IPA） _(★0, Swift)_
- [discord-bot](https://github.com/blackmichael/discord-bot) — A silly discord bot. Written in Go, powered by Jev. _(★0, Go)_
- [jev-email-classifier](https://github.com/AkashNaickar/jev-email-classifier) — Chrome MV3 extension that classifies Gmail rows with TypeSafe Jev (Choice/Score/Noul). Metadata-only, read-only, bring your own key. _(★0, TypeScript)_
- [mindrails-supervisor](https://github.com/haskallalk-eng/mindrails-supervisor) — Pick the right AI model and effort before an agent starts: Jev plugins for Claude Code and Codex, a local chat app for both, and an MCP completion gate. _(★0, JavaScript)_
- [last-lst97-dev-web](https://github.com/lst97-oss/last-lst97-dev-web) — Simple personal profolio plus chat assistance with RAG and Jev _(★0, TypeScript)_
- *16 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Finance & Trading (51)

- [quantdinger](https://github.com/OpenByteInc/QuantDinger) — Open-source AI Trading OS, agent trading, and vibe trading, with Jev System One integration. Research, build Python strategies, backtest, and paper/live trade across crypto, stocks, and forex. Launch your own multi-tenant trading SaaS with  _(★12397, Python)_
- [jev-trader](https://github.com/jarrodwatts/jev-trader) — One AI trade decision every Monad block. Jev on Kuru MON-USDC. _(★2758, TypeScript)_
- [aistock](https://github.com/EthanAlgoX/AIStock) — One person can become their own super-analyst. Try it online: https://myaistock.top _(★339, Python)_
- [jev-trade](https://github.com/aowang-ai/jev-trade) — Live Jev trader on Hyperliquid _(★183, TypeScript)_
- [JevGym](https://github.com/ruyianry/JevGym) — JevGym is an open-source platform designed to benchmark and facilitate better probabilistic estimation in Jev-alike models _(★104, Python)_
- [jev-trades](https://github.com/zadescoxp/Jev-Trades) — Trading bot with the all new TypeSafe AI's first system one model named as Jev _(★32, Python)_
- [jev-quantum](https://github.com/karminski/Jev-Quantum) — 亚微秒级 System-1 模型，准确率服从高斯分布 _(★31, Rust)_
- [smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub) — Read-only trading journal and review harness: Jev typed judgments, agent integration, and a reproducible finance benchmark. No orders, no advice. _(★27, Python)_
- [jev-trader](https://github.com/buberlo/jev-trader) — 24/7 market-making system around Jev (TypeSafe System One) decisions: deterministic state, calibrated judgments, hard risk vetoes. _(★20, Python)_
- [jevocks](https://github.com/unicodeveloper/jevocks) — Everyday Stocks Status with Jev _(★19, TypeScript)_
- [polymarket-btc5m-jev-trading](https://github.com/VGabriel45/polymarket-btc5m-jev-trading) — 5m BTC Up/Down Polymarket trading agent using Typesafe Jev as the decision layer & TUI _(★18, TypeScript)_
- [jev_stock](https://github.com/sosopop/jev_stock) — An experimental JEV-powered framework for forecasting short-term stock price direction from structured market data. _(★14, Python)_
- [trade-jev](https://github.com/justinhe16/trade-jev) — Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data _(★9, Python)_
- [moomoo-jev-trader](https://github.com/maxlibin/moomoo-jev-trader) — Live Moomoo trading dashboard with TypeSafe Jev market reviews _(★6, Python)_
- [jev-realtime-trading](https://github.com/rthomas24/jev-realtime-trading) — Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app. _(★5, TypeScript)_
- [veyra](https://github.com/iamngoni/veyra) — Autonomous, provider-neutral trading service in Rust. LLM and Jev decisions pass a deterministic risk gate before any MT4 order; includes an operations console. _(★4, Rust)_
- [jev-as-quant](https://github.com/jiayylu/jev-as-quant) — Typed System-1 decisions (Laya/Jev) as the judgment layer of a quant research stack, with Claude as System 2. Requirements → design → code → experiments. _(★3, Python)_
- [jev-a-share-trader](https://github.com/Eric-Zhou-0302/jev-A-share-trader) — A Jev-powered technical analysis workspace for China A-shares, supporting AKShare/Tushare, market scans, and Buy/Hold/Sell assessments with time horizons and traceable evidence. _(★2, Python)_
- [jev-alpha-bench](https://github.com/Gaurav-Gosain/jev-alpha-bench) — Does Jev predict stock returns from news? It reads the news well; there is no tradeable alpha. Three arms separate reading from recall. _(★1, Go)_
- [financialpredictionjev](https://github.com/thodoh1/FinancialPredictionJev) — Using Jev to test how well it predicts financial markets(just like most llms as of september 2026, it doesnt do that good) _(★1, Python)_
- [jev-finance-benchmark](https://github.com/hifizz/jev-finance-benchmark) — typesafe.ai model jev finance benchmark _(★1, n/a)_
- [trading-bot-jev](https://github.com/Spykoninho/trading-bot-jev) — Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news _(★1, TypeScript)_
- [jev-paper-trader](https://github.com/MojoAI-King/jev-paper-trader) — Paper trading real Polymarket and Kalshi markets with a fake $100k: can Jev + Claude research beat the market? _(★1, Python)_
- [fuzzy-jev](https://github.com/dsaad68/fuzzy-jev) — Ask Jev typed questions about text and get calibrated probabilities back, then turn them into decisions with fuzzy rules (AND, OR, NOT, hedges, Mamdani outputs) and draw the rule base as SVG. A CLI and a Rust library (native and wasm32). _(★1, Rust)_
- [jev-trader](https://github.com/gilesknap/jev-trader) —  _(★0, Python)_
- [trading-jev](https://github.com/mariobgsp/trading-jev) — Momentum screen for the IDX gorengan band. A model decides the entry; a journal scores whether it was right. _(★0, Python)_
- [jev-vs-deepseek](https://github.com/jupiutrera/jev-vs-deepseek) — Demo: un LLM tradicional (DeepSeek) contra Jev decidiendo en un control de seguridad de aeropuerto contrarreloj _(★0, TypeScript)_
- [S1Q](https://github.com/CYMCharming/S1Q) — S1Q: low-bit quantization for Jev-like System One decision models. Kev, NanoJev, Laya; reproducible paired evaluations. _(★0, Python)_
- [gsp](https://github.com/Shivam-Jha96/gsp) — An AI-driven macro-sentiment analysis terminal that reads thousands of breaking global financial news events in real-time, scores their market impact using a custom Contrastive-LM System-One model on a serverless GPU! _(★0, Python)_
- [QuantVault-Jev](https://github.com/Dento77384/QuantVault-Jev) — Paper-trading scaffold: brainbrick-trades strategy vault + TypeSafe Jev judgments, with a Streamlit dashboard _(★0, Python)_
- [jevtrade](https://github.com/Theo-Gkisis/jevtrade) —  _(★0, n/a)_
- [btc_lab](https://github.com/adrianforsenmusic/btc_lab) — Paper-trading-labb för BTC med TypeSafe Jev — bara papper, ärliga mätningar _(★0, Python)_
- [jevcrypto](https://github.com/gignac-cha/jevcrypto) — Generate prompt-influenced UUID strings with Jev through TypeSafe or OpenRouter. _(★0, TypeScript)_
- [orch](https://github.com/Lucasarkh/orch) — Orquestrador de agentes Claude no terminal: o Jev (TypeSafe) escolhe o modelo mais barato capaz, verifica o resultado e escala quando preciso. _(★0, Go)_
- [jevtrader](https://github.com/zd87pl/jevtrader) — Local-first SEC 8-K research lab: score filings point-in-time with Jev, OpenAI or local LLMs, and label which results can count as evidence. Never places orders. _(★0, Python)_
- [jev-rag](https://github.com/kanishka-namdeo/jev-rag) — Local-first hybrid RAG: traditional vs Jev-style (System One) pipelines over your own documents — with a built-in benchmark lab (6 scenarios, 48 questions, independent LLM judge). Hybrid won +8.4pp correctness at identical cost. _(★0, JavaScript)_
- [aotn-jev-invoices](https://github.com/tameernoor/aotn-jev-invoices) — Jev judges invoices, code decides. Companion code for the article "The classifier you don't have to train". _(★0, Python)_
- [jev-crypto-scout](https://github.com/yasdelayu/jev-crypto-scout) — Crypto screening: quant signals in code (CoinGecko), news judgment via Jev (TypeSafe System One) — sentiment/catalyst/confirmed, not a trading bot _(★0, Python)_
- [JevPip](https://github.com/yo4e/JevPip) — GMOのFX/BTC市場データに対応したローカル市場研究ターミナル。ライブチャート、ペーパートレード、バックテスト、安全監督、TypeSafe Jev連携。安全機構を整えたうえで実売買対応予定。 _(★0, Python)_
- [JEV_Coin](https://github.com/theman001/JEV_Coin) — Jev AI (TypeSafe System One) crypto scalping long/short paper-trading bot with web monitor (Docker/ARM64/OMV) _(★0, Python)_
- [jev-trader](https://github.com/JienWeng/jev-trader) —  _(★0, Python)_
- [bit-jev](https://github.com/Zeaulo/bit-jev) — Kev-style structured decisions on BitNet with a native I2_S CPU path (source preview) _(★0, Python)_
- [jevai_trade_bot](https://github.com/burak-alp/jevai_trade_bot) —  _(★0, Python)_
- [ghost-ops-jev-buildathon](https://github.com/sumithshridhar/ghost-ops-jev-buildathon) — Team Ghost Ops, Jev Buildathon: guard rules that mak the Ledger finance agent unable to lose money, whil it keeps paying real bills. 59/59 scenario tests. _(★0, n/a)_
- [JevSentinel](https://github.com/ORiONx888/JevSentinel) — Real-time token risk intelligence and early-warning protection engine for crypto alert systems. Built around JEV with behavioral, wallet, market, liquidity, and security intelligence. _(★0, JavaScript)_
- [jev-screen](https://github.com/YuanTong-Wu/jev-screen) — Turn an investment idea into an evidence-backed stock list: Jev reads ~20k global companies and checks official annual reports. 主题选股 / 产业链 / 年报证据 — runs locally via your AI agent. _(★0, Python)_
- [jev-rag-gate](https://github.com/breaker364/jev-rag-gate) — Semantic gating for RAG retrieval candidates (relevance, premise contradiction, prompt injection) using the TypeSafe Jev System One model _(★0, Python)_
- [jev-quant](https://github.com/itsadrianxv/jev-quant) — C++ trading system leveraging TypeSafe Jev. _(★0, C++)_
- [kblam](https://github.com/hungryboygeorge/kblam) — kblam: the knowledge base for LLM-assisted mereology. it's a flat-file research/knowledge storage system with enforced organization (using heuristics, semantic similarity, and Jev evaluation) to prevent document drift, internal contradictio _(★0, Python)_
- [vizardpad](https://github.com/justbiar/vizardpad) — Scenario launchpad for MonadBFT: break Category Labs' real monad-bft consensus in your browser, with DeFi what-ifs, AI agents (Jev) and MON / x402 payments. _(★0, TypeScript)_
- *1 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Safety, Routing & Guardrails (276)

- [Intent-Router](https://github.com/angel291592/Intent-Router) — Intent compiler for AI agents — converges vague requests into typed IntentSpec contracts (probe, ask, or halt before routing), the input layer for routers and typed-decision models like Jev & Laya _(★668, Python)_
- [jev-review](https://github.com/devagrawal09/jev-review) — A staged code-review workflow and local dashboard built with TypeSafe Jev. _(★661, TypeScript)_
- [jev-router](https://github.com/gargpratyush/jev-router) — Route to the cheapest model in claude code for your task using jev-router _(★525, JavaScript)_
- [jevrouter](https://github.com/BillionsBobby/JevRouter) — A lightweight Jev-powered router for models, tools, and subagents _(★362, TypeScript)_
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) — Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn. _(★274, JavaScript)_
- [jev-review](https://github.com/NiazMorshed2007/jev-review) — Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev. _(★231, TypeScript)_
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) — grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with AND/OR/NOT. 意味で探す grep。日本語で英語を、英語で日本語を検索できる _(★144, JavaScript)_
- [jevmeter](https://github.com/ChetasLua/jevmeter) — Put a live Jev (TypeSafe) meter on any video: every sentence scored, rendered as a 16:9 edit _(★105, Python)_
- [jevals](https://github.com/openlayer-ai/jevals) — Agent evals and guardrails as Jev decisions: one request per trace, a fraction of a cent, fast enough for the agent loop. Runs locally with Kev or Laya. _(★102, Python)_
- [agent-router](https://github.com/nidhi-singh02/agent-router) — CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr _(★100, TypeScript)_
- [jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge) — Using Jev as an evaluator. _(★98, Python)_
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) — Route HTTP requests by meaning. A semantic router for Hono powered by Jev. _(★50, TypeScript)_
- [jev-code-reviewer](https://github.com/egma-ai/jev-code-reviewer) — Review behavior, not just diffs. Jev prioritizes human attention; OpenAI explains the changes. Local CLI + agent skill + GitHub extension. _(★46, JavaScript)_
- [jev-tree](https://github.com/Chuf-H/jev-tree) — Jev-native probability tree and graph runtime for verifiable multi-step decision making. _(★42, Python)_
- [jev-guard](https://github.com/klauswg/jev-guard) — Real-time risk triage gateway for exchange deposits and withdrawals — Jev (TypeSafe System One) handles triage only; adjudication stays in deterministic code. _(★36, Java)_
- [jev-guard](https://github.com/leepokai/jev-guard) — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, checks skills and plugins. Claude Code, Codex, Copilot, Gemini, Cursor, pi, OpenCode,  _(★34, JavaScript)_
- [jev-reviewer](https://github.com/choxos/jev-reviewer) — Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with it _(★34, JavaScript)_
- [jevembed](https://github.com/HITsz-TMG/JevEmbed) — Meet JevEmbed — turn embeddings into decisions. Choose, score, and judge with your choice of embedding model. _(★26, Python)_
- [jevalyn](https://github.com/Ray-Hughes/jevalyn) — The decision layer for your Rails app. A Rails-native wrapper around TypeSafe's Jev System One API: typed, calibrated decisions in your control flow. _(★20, Ruby)_
- [jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling) — Self-hosted AI email classifier for Gmail powered by Jev. Create custom labels, organize your inbox, and filter spam with confidence and cost controls. _(★19, JavaScript)_
- [jeval](https://github.com/rlaope/jeval) — Measures what your Jev classifier's confidence is really worth, and sets the human hand-off line from what a mistake costs. _(★19, Python)_
- [harness-router](https://github.com/Protocol-Lattice/harness-router) — Fast decision routing for agent harnesses — native MCP with Jev for tool selection and MCTS for multi-step decisions. _(★19, Python)_
- [BrighTO_Router](https://github.com/thusinh1969/BrighTO_Router) — BrighTO LLM Router: free open-source, ultra-fast self-hosted Rust LLM gateway for OpenAI/Anthropic APIs, SystemOne/JEV/DJEV decisions, Ollaya/Laya, load balancing, fallback routing, team keys and token budgets. _(★18, Rust)_
- [a3m-router](https://github.com/Das-rebel/a3m-router) — ⚡ Adaptive multi-model LLM router — 80+ providers, Jev System One single-pass routing (model=jev-auto), pheromone-trail failover, parallel ensemble merge. npm: adaptive-memory-multi-model-router _(★17, TypeScript)_
- [pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) — Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway _(★14, JavaScript)_
- [snapjudge](https://github.com/Micha0827/snapjudge) — Typed decisions (choice / score / yes-no) from local Qwen models on Apple Silicon. Probabilities come straight from the logits, no text generation. TypeSafe-compatible HTTP API, runs on MLX. _(★14, Python)_
- [jev-router](https://github.com/prismhq/jev-router) — Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM _(★13, Python)_
- [pi-jev-router](https://github.com/philippdubach/pi-jev-router) — A minimal Pareto-optimal OpenRouter model router for pi, based on Jev _(★13, TypeScript)_
- [WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) — evals.typesafe.ai workflow code published _(★13, Python)_
- [pi-jev-router](https://github.com/win4r/pi-jev-router) — Task-boundary model routing for Pi Coding Agent, powered by TypeSafe Jev. Conservative policies, exact caching, and observable failover. _(★12, TypeScript)_
- [clean-code-review](https://github.com/frostney/clean-code-review) — Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js. _(★11, TypeScript)_
- [jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot) — Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev _(★11, TypeScript)_
- [pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router) — Route pi prompts to task-appropriate model tiers with TypeSafe Jev typed judgments. Budget-aware, with automatic fallback. _(★11, TypeScript)_
- [pdf-race](https://github.com/goodrahstar/pdf-race) — Docling → Jev vs Docling → Gemini 3.8 Flash vs Gemini reading the PDF: same documents, one clock, scored against arXiv's own metadata _(★10, JavaScript)_
- [jev-router](https://github.com/rajdhakad9826/jev-router) — LLM router that picks the cheapest model capable of handling a query, using TypeSafe's Jev for fast classification instead of an LLM call. _(★9, TypeScript)_
- [pi-jev](https://github.com/iefnaf/pi-jev) — Pi extension suite powered by Jev: selective context compaction and model routing _(★9, TypeScript)_
- [lejudge-jev-jepa](https://github.com/AbdelStark/lejudge-jev-jepa) — Natural-language constraints for JEPA world-model planning, judged by a decision model instead of an LLM. _(★9, Python)_
- [twitter-jev-guard](https://github.com/qs-lll/twitter-jev-guard) — 使用 TypeSafe Jev 在 X/Twitter 时间线上识别低质量、垃圾和广告帖子，并在文字区域显示醒目的半透明水印。 _(★9, JavaScript)_
- [jev-risk-check-provider](https://github.com/caiovicentino/jev-risk-check-provider) — x402 risk-check provider: TypeSafe Jev (System One) typed decisions + ES256-signed attestations for agent payments _(★9, TypeScript)_
- [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) — Check whether each cited paper supports the sentence citing it. Claude proves the quote, TypeSafe's Jev scores it, a human decides. _(★8, JavaScript)_
- [jev-tool-router](https://github.com/jackbarunz/jev-tool-router) — Jev-powered MCP tool routing for Codex _(★8, JavaScript)_
- [opencode-jev-router](https://github.com/robertn702/opencode-jev-router) — Adaptive reasoning effort for OpenCode via Jev, with an in-process plugin and Responses API proxy _(★8, TypeScript)_
- [tia](https://github.com/benjamincanac/tia) — Triage Issue Agent for GitHub, built with Eve and Jev. _(★8, TypeScript)_
- [pi-shift-router](https://github.com/green-dalii/pi-shift-router) — Per-turn model routing for the Pi coding agent: a small judge picks the cheap or the strong tier for each message, with multi-model failover, task-level orchestration, and an optional decision-model judge (Jev) that answers with a calibrate _(★8, TypeScript)_
- [jev-auto-router](https://github.com/miniLV/Jev-Auto-Router) — Jev Auto Router (Jev Router): experimental per-call GPT model routing for Codex via TypeSafe Jev and a local Responses proxy, with independent task verification. _(★7, TypeScript)_
- [jev-guard](https://github.com/muratcakmak/jev-guard) — Probability-scored guardrails for Claude Code: deny rule-breaking edits and unasked-for deploys, route your docs into each prompt, and check the final answer against the turn's own evidence. _(★7, TypeScript)_
- [jev-dimabsa](https://github.com/ZhangYiqun018/jev-dimabsa) — TypeSafe Jev baseline for DimABSA (SemEval-2026 Task 3) subtask 1: zero-shot and 3-shot valence-arousal regression _(★7, Python)_
- [jev-ai-sdk-form-router](https://github.com/vercel-labs/jev-ai-sdk-form-router) — Route form submissions to the right people with Jev and AI SDK. _(★6, TypeScript)_
- [typesafe-jev-incident-router](https://github.com/kyle-chalmers/typesafe-jev-incident-router) — Confidence-gated incident routing with TypeSafe Jev _(★6, Python)_
- [jev-papers](https://github.com/stas4000/jev-papers) — 1,000 arXiv AI papers classified with one Jev decision each, checked against an LLM judge. Open rebuild, MIT. _(★6, Python)_
- *226 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### Productivity & Knowledge (30)

- [jevharness](https://github.com/TianyuCodings/JevHarness) — LLM-authored task-specific Jev harnesses with optional full-trajectory reward reflection and GEPA evolution. _(★506, Python)_
- [dasheng](https://github.com/wquguru/dasheng) — 大声读 — R2T2 流式 ASR 听，Jev 逐词判，英文朗读评分 _(★139, JavaScript)_
- [Jevstiller](https://github.com/tomerglick57/Jevstiller) — Distill a repeated Jev classification task into a local model, on the fly — same answers, your hardware. _(★60, Python)_
- [jev-design](https://github.com/bilune/jev-design) — Can a model design a dashboard? A console whose whole design system is generated at runtime by Jev from a one-sentence brief. _(★55, TypeScript)_
- [jevgraph](https://github.com/chenmingtang830/jevgraph) — Evidence-backed knowledge graph construction with typed Jev relation decisions _(★22, Python)_
- [discoprint](https://github.com/lirantal/discoprint) — Classify an artist's discography by theme, mood, and lyrical complexity with Jev (TypeSafe AI), and view it as a colorful terminal dashboard _(★4, JavaScript)_
- [todo-jev](https://github.com/maker-KK/todo-jev) — ⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One) _(★4, Python)_
- [jevpdf](https://github.com/kylemclaren/jevpdf) — Ask a PDF in your own words and watch the matching lines light up. React + pdf.js + TypeSafe Jev. _(★3, TypeScript)_
- [jevslop](https://github.com/TKY-27/JevSlop) — Jevによるnote記事のAI Slop判定サイト _(★3, TypeScript)_
- [candidate-experience-benchmark](https://github.com/adambkovacs/candidate-experience-benchmark) — Compare TypeSafe Jev and LLMs on 60 synthetic candidate-experience reviews: four classification tasks, prompt variants, costs, tokens, and reproducible evidence. _(★3, HTML)_
- [pi-jev-todo-audit](https://github.com/xz-dev/pi-jev-todo-audit) — Pi extension that audits rpiv-todo board drift every 10 agent loops using TypeSafe's jev model, injecting corrective nudges when the agent wanders off-task _(★3, TypeScript)_
- [jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction) — Parsing the PDF and extracting the relevant information _(★2, Python)_
- [tempo-jev-demo](https://github.com/mychaelangelo/tempo-jev-demo) — A natural-language task workspace comparing performance across AI models (TypeSafe's Jev, GPT-5.6 Luna, and Gemini 3.8 Flash) _(★2, TypeScript)_
- [taskpenny](https://github.com/cintocasals/taskpenny) — Frontier prices only for frontier work: each task goes to the cheapest model that does it well, a request is split only when that pays, and every result is checked. Decisions by Jev. _(★1, Python)_
- [JevGraphBench](https://github.com/VictorYXL/JevGraphBench) — Benchmarking Jev’s Capabilities on Graph Tasks _(★0, Python)_
- [canmou-clipper](https://github.com/baocanmou/canmou-clipper) — 参谋剪藏：把网页存进 Obsidian，由 Jev 判断归档目录和标签的 Chrome 扩展 | Chrome extension that clips web pages to Obsidian and lets Jev pick the folder and tags _(★0, TypeScript)_
- [centurion](https://github.com/RobertoDure/centurion) — Send logs from any system to Kafka. Centurion consumes them one by one, asks Jev to evaluate each log against your rules, flags the matches, runs actions, and streams everything to a dashboard in real time. _(★0, JavaScript)_
- [jev-in-education](https://github.com/yamnor/jev-in-education) — Supplementary materials for note articles testing Jev (TypeSafe AI) for reading student answers in education _(★0, n/a)_
- [arjev](https://github.com/harmoniqs/arjev) — arjev — a daily arXiv digest engine that ranks against your living Obsidian vault: deterministic lexical front-line, Jev confidence-gated rerank, and a learning loop where your own notes are the ground truth. _(★0, Python)_
- [jev-pr-quality](https://github.com/rawtreedb/jev-pr-quality) — Jev-assisted pull request quality reviews and a multi-repository RawTree dashboard _(★0, TypeScript)_
- [jev-visualizer](https://github.com/jsonclem/jev-visualizer) — A gamified visualizer for executing tasks with Jev and Agentic systems _(★0, TypeScript)_
- [jev-study](https://github.com/wjdjdakf17/jev-study) — Jev(TypeSafe AI System One Model) 스터디 — 타입화된 결정·RLCD·confidence-gated routing을 한국어 노트와 TypeScript 목업으로 정리 _(★0, TypeScript)_
- [jev](https://github.com/taifoon-io/jev) — Grade an AI agent's job with TypeSafe's Jev: did it do the work as the task laid it out? Facts first, Jev on your own key, a receipt, and optional on-chain records. _(★0, TypeScript)_
- [jev-dashboard](https://github.com/rockomatthews/jev-dashboard) —  _(★0, TypeScript)_
- [Jev-dashcam](https://github.com/Gackson/Jev-dashcam) — Native macOS app that captures foreground window content and organizes it into topics with Jev. _(★0, Swift)_
- [jevlike](https://github.com/yorshstudent-a11y/jevlike) — Train a compact model to pick one option from a changing list in a single pass, no autoregressive generation needed. _(★0, Python)_
- [woo-note-triage](https://github.com/hamzaahmadaslam/woo-note-triage) — Note Triage for WooCommerce: a WordPress plugin that sorts customer order notes (gift message, delivery instruction, question, complaint, fraud signal) with TypeSafe's Jev model and flags the urgent ones for staff. _(★0, PHP)_
- [jev-watch](https://github.com/polaminggkub-debug/jev-watch) — Watchdog for AI coding agents: stops Codex/OpenCode when they loop, stall or drift off task, then resumes the same session with a correction. Built for Claude Code orchestrators. Uses Jev via OpenRouter. _(★0, JavaScript)_
- [commit-changelog](https://github.com/hamzaahmadaslam/commit-changelog) — Turns free-form git commits into a Keep a Changelog section: each commit's own first line, placed by its conventional-commit prefix or by TypeSafe's Jev model, with unsure commits listed for review. _(★0, JavaScript)_
- [jev-bookmarks](https://github.com/quolu/jev-bookmarks) — Chrome履歴から目的に合うページを選び、Jevで操作して役立ったURLだけをプロジェクトごとに記録するCLI _(★0, Python)_

### Media & Content (34)

- [imajev](https://github.com/mohit67890/imajev) — Open Jev-style typed-decision model that also takes images: photo + app state + typed questions in, calibrated probabilities out, locally. _(★253, Python)_
- [hyperedit](https://github.com/kevinbadi/hyperedit) — AI-powered video editor with FFMPEG, Remotion, & Obsidian Agents Baked in - POWERED BY JEV  _(★207, TypeScript)_
- [JEV_sees](https://github.com/CharlesFeng0314/JEV_sees) — Eyes are All JEV Needs - real time visual devisions from RGB, video and RGB-D cameras. _(★173, Python)_
- [jevois](https://github.com/jevois/jevois) — JeVois smart machine vision framework _(★164, C)_
- [jevonscameraviewer](https://github.com/j-east/JevonsCameraViewer) — An app for viewing multiple video streams from USB cameras. Low cost real time eye tracking. You can rotate and mirror the images and also use a variety of filters. Easily take screenshots. Very useful for c270 hacks. Exposure lock and some _(★162, C#)_
- [OneJev](https://github.com/OmniJev/OneJev) — 🚀🚀 A multimodal System One decision model that gives calibrated answers to typed questions about screens, photos, video and text in one forward pass. _(★113, Python)_
- [jev-voice](https://github.com/kevinbadi/jev-voice) — Talk to your Mac. Local whisper.cpp + one Jev (TypeSafe) call per command + macOS automation. _(★107, Python)_
- [youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) — Detect youtube sponsor segment with live audio and transcript powered by Jev _(★97, JavaScript)_
- [jev-paint](https://github.com/achimala/jev-paint) — Use Jev to make art! _(★58, JavaScript)_
- [live-jev](https://github.com/okinaaudio/live-jev) — Control Ableton Live with one short sentence (Japanese / English). Summon with ⌘⇧Space, type or dictate, done. _(★42, Python)_
- [jevclip](https://github.com/cclank/jevclip) — Jev-powered video highlights and cited summaries from subtitles and scripts _(★24, Python)_
- [transcript-lens](https://github.com/sensahin/transcript-lens) — YouTube transkriptlerini anlamına göre keşfedin. Türkçe arayüz, Jev analizi, altyazı dışa aktarma ve Vercel kurulum rehberi. _(★18, TypeScript)_
- [jevthoven](https://github.com/cocktailpeanut/jevthoven) — AI Music (MIDI) generator powered by Jev _(★15, TypeScript)_
- [jev-yt-time-saver](https://github.com/jaibhasin/jev-yt-time-saver) — A Chrome extension that covers distracting YouTube videos with Jev. Show anyway whenever you want. _(★6, JavaScript)_
- [Decis](https://github.com/chaitin/Decis) — Self-hosted, Jev-compatible decision-model API — one /v1/systemone endpoint, open weights (Laya, kev), one Docker image per engine. _(★6, Python)_
- [jev-shield](https://github.com/vmendes90/jev-shield) — Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev _(★5, TypeScript)_
- [jev-music-tag](https://github.com/xhongc/jev-music-tag) — 利用 jev 刮削音乐元数据,风格,语言 _(★5, Python)_
- [jauvex](https://github.com/reindent/jauvex) — Your coding agents, side by side, by voice. Claude, Codex & Grok in one desktop app, with Jev for the fast decisions. _(★5, TypeScript)_
- [smart-switch](https://github.com/reycn/smart-switch) — Reimagined window switcher for macOS using frontier artificial intelligence. Predicted by TypeSafe's Jev model _(★4, Swift)_
- [jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control) — Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app. _(★4, Swift)_
- [jevcut](https://github.com/VBS2004/jevcut) — Auto-clipper that turns long videos (podcasts, talks, essays, comedy) into short standalone clips for Shorts, Reels and TikTok. Code lists every possible cut; an AI judge picks where each clip starts and ends. Benchmarked on 38 hand-labelle _(★4, Python)_
- [jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper) — Low-latency audio censorship POC using Jev typed decisions and ffmpeg. _(★3, TypeScript)_
- [emoji-jev](https://github.com/colinmcdermott/emoji-jev) — Emoji autocomplete at the speed of typing. TypeSafe AI Jev on a Whop-hosted TanStack Start app. _(★3, TypeScript)_
- [vev](https://github.com/Xiaooolong/vev) — Jev-like decision models that can also see images — open weights on Qwen3.5, run on your own GPU _(★2, Python)_
- [mimicry](https://github.com/jxucoder/mimicry) — Rewrite AI drafts in your own voice with a bounded TypeSafe feedback loop. _(★1, Python)_
- [typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) — Diffusion-style pixel art out of a general classifier (TypeSafe Jev): 256 parallel pixel questions + refinement passes _(★1, HTML)_
- [jevlens](https://github.com/knowlet/jevlens) — Chrome extension for annotating articles, X/Twitter posts, and Threads posts. _(★1, JavaScript)_
- [audio-jevlike](https://github.com/alperiox/audio-jevlike) — Prosodia: an audio-native Jev-shaped decision model — typed calibrated decisions from speech, no ASR _(★1, Python)_
- [ai-dj](https://github.com/yask123/ai-dj) — An AI with its hands on the decks: real songs, real DJ moves, every move a tool call decided live by Jev in ~150 ms _(★1, Swift)_
- [VoiceControlledWebApp-Jev](https://github.com/kundan1293/VoiceControlledWebApp-Jev) — A web app to controlled web page using Jev API. _(★0, n/a)_
- [jev-voice](https://github.com/dgr8akki/jev-voice) — Voice control for Chrome: open sites, search, click links and fill in forms hands-free. MV3 extension, on-device speech recognition, bring your own TypeSafe or Vercel key. _(★0, JavaScript)_
- [imagejev](https://github.com/guangshinhaha/imagejev) — Open System 1 decision engine for images: typed choice/score/bool decisions in one forward pass, calibrated _(★0, Python)_
- [jev-cut](https://github.com/chenbaiyujason/jev-cut) — Music-driven anime editing with jev decision models, FreeCut, and reproducible media preparation. _(★0, TypeScript)_
- [aphasia-word-finder](https://github.com/nautahakk/aphasia-word-finder) — For people with aphasia: describe the word you can't find, tap the right guess, hear it said. It only picks from a fixed word list plus your own names, using Jev by TypeSafe. _(★0, JavaScript)_

### Mobile & Desktop Apps (22)

- [tiptour-macos](https://github.com/milind-soni/tiptour-macos) — Open-Source fast local computer use _(★670, Swift)_
- [keel](https://github.com/codejunkie99/keel) — Local-first macOS coding workspace with local Laya and optional Jev decision selection _(★324, Rust)_
- [rikkahub-sillytavern-android](https://github.com/MiaoWuNYA/rikkahub-sillytavern-android) — 安卓AI聊天端:无损导入酒馆卡，缓存强省用量，Jev 决策，多维记忆，QQbot，AI群聊，酒馆主题，插件系统，强兼容中转站。手机移动端原生支持/Android AI Chatbox: lossless SillyTavern card import, aggressive cache optimization, Jev decisions, multi-dimensional memory, anti-blank-reply, proactive messages, AI  _(★67, Kotlin)_
- [jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop) — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token. _(★23, JavaScript)_
- [jev-block-android-ad](https://github.com/ufec/jev-block-android-ad) — JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   an _(★6, Kotlin)_
- [jev-android](https://github.com/dougsong/jev-android) — A Kotlin Android SDK for UI automation powered by TypeSafe Jev, with an accessibility runtime and sample app. _(★5, Kotlin)_
- [macos-computer-use-kit](https://github.com/Sur-Cai/macos-computer-use-kit) — AX-first computer use for AI agents on macOS with optional Jev (TypeSafe System One) semantic guards: calibrated target/input judgments before an irreversible action, decisions kept in code. Accessibility-tree targeting, window-scoped input _(★4, Python)_
- [pocketjev](https://github.com/NullPo-jp/PocketJev) — On-device iPhone visual decision tool using MLX and Qwen3-VL direct option logits. _(★2, Swift)_
- [windowsjev](https://github.com/Teylersf/WindowsJev) — Token-efficient Windows automation and durable research MCP server for Codex and Claude Code, powered by TypeSafe Jev. _(★1, C#)_
- [JEVIL-uninstaller](https://github.com/severs65/JEVIL-uninstaller) — A lightweight portable Windows uninstaller with leftover cleanup, Appx/UWP support and Safe Mode removal. _(★1, C++)_
- [droidjev](https://github.com/mkruglikov/droidjev) — A fast, screenshot-free Android emulator clicker powered by TypeSafe's jev _(★0, JavaScript)_
- [jev-harness](https://github.com/Cleobury/jev-harness) —  Push-to-talk voice control for Windows: local Whisper, Windows OCR and TypeSafe's Jev model decide what to click, type and open. _(★0, Python)_
- [Navi](https://github.com/LiamCarlin/Navi) — Jev-powered Spotlight replacement for macOS — typed fast decisions, Claude for answers and computer use, local screen memory into an Obsidian vault _(★0, Swift)_
- [jev-supervisor](https://github.com/ryyyzer/jev-supervisor) — DeepSeek Harness macOS 客户端的 Jev 执行监督插件，支持自有 TypeSafe Key、决策检查与可配置预算。 _(★0, JavaScript)_
- [jev-emoji](https://github.com/seulkikaang/jev-emoji) — A native macOS emoji picker using TypeSafe Jev typed decisions _(★0, Swift)_
- [speed-reading-app](https://github.com/TomySpagnoletti/speed-reading-app) — Read AI coding agent outputs in seconds. Jev, TypeSafe's decision model, highlights what needs your decision or action and dims the rest. Tauri + CodeMirror app for macOS. _(★0, TypeScript)_
- [Smithy-Windows](https://github.com/Divhanthelion/Smithy-Windows) — Smithy for Windows: a native Rust IDE and coding agent on your own model, with Jev checking every step and unattended Runs that turn one sentence into tested commits. _(★0, Rust)_
- [jev-cua](https://github.com/edgeteamio/jev-cua) — Voice-controlled Mac computer use on TypeSafe Jev: speech to typed decisions to verified accessibility actions, no screenshots to a big model _(★0, Swift)_
- [mobile-jev](https://github.com/Capitalofgeorgiapolitician1569/mobile-jev) — Automate real Android tasks on live phones with Jev, Mobilerun, and TypeSafe—no ADB needed. _(★0, n/a)_
- [cacador-de-anuncios](https://github.com/vibecodingelite-ai/cacador-de-anuncios) — Extensão do Chrome que analisa anúncios da Biblioteca de Anúncios da Meta com o JEV (typesafe/jev-1.13) via OpenRouter: chance de resultado, ângulo, gancho e nicho. Sua chave fica só no seu navegador. _(★0, JavaScript)_
- [jevcast](https://github.com/RyanErkal/jevcast) — Native macOS launcher and window manager. Optional natural-language matching with Jev by TypeSafe AI. _(★0, Swift)_
- [JevSceneMiner](https://github.com/bskkimm/JevSceneMiner) — Mine driving scenes from logs with Jev: scene text in, scenarios with probabilities and timestamps out. _(★0, Python)_

### Home, IoT & Robotics (10)

- [embodied-jev](https://github.com/FBddcz/embodied-jev) — EmbodiedJev: MuJoCo robot decision workbench with MiniCPM5-2B, Jev and compatible model APIs _(★254, Python)_
- [jev-drone](https://github.com/RomanSlack/jev-drone) — Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz _(★235, Python)_
- [bicameral](https://github.com/AbdelStark/bicameral) — Hybrid coding harness: System 2 writes, System 1 (Jev) runs reflexes. _(★7, TypeScript)_
- [jev-robotics-demo](https://github.com/FazalAAli/jev-robotics-demo) — Jev (TypeSafe System One) vs Claude Opus 5 driving a simulated robot arm in MuJoCo _(★5, Python)_
- [typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo) — Three.js drone simulator with a Python backend and live TypeSafe Jev navigation _(★2, Python)_
- [ha-gutcheck](https://github.com/funkadelic/ha-gutcheck) — Home Assistant integration that uses TypeSafe AI's Jev to spot problems and suggest cleanups in your install, and asks before changing anything _(★2, Python)_
- [jev-home-assistant-sentinel](https://github.com/bojansandhaus/jev-home-assistant-sentinel) — A safety boundary for AI-assisted Home Assistant decisions, with explicit policy checks and deterministic state verification. _(★1, Python)_
- [jev-robot](https://github.com/arterialist/jev-robot) — A Unitree G1 in MuJoCo with JEV reflexes, Gemini planning, and a live browser control room. _(★0, Python)_
- [HA-Crop-Steering-Jev](https://github.com/JakeTheRabbit/HA-Crop-Steering-Jev) — Crop Steering, Jev edition: the HA crop-steering engine with TypeSafe Jev judging every decision across P0-P3, probes, shots, salt and alerts, inside a deterministic safety envelope. _(★0, HTML)_
- [JevHomeAssistant](https://github.com/wantosure/JevHomeAssistant) —  _(★0, Kotlin)_

### Awesome Lists & Catalogs (87)

- [awesome-jev](https://github.com/yibie/awesome-jev) — A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions. _(★2101, Python)_
- [awesome-jev](https://github.com/heyjunpenn/awesome-jev) — A verified, community-maintained catalog of 916 open-source projects built with Jev. _(★919, Astro)_
- [awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) — Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software. _(★895, Python)_
- [awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) — A curated list of tools  built for Jev — TypeSafe AI's System One model for typed decisions. _(★740, n/a)_
- [awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) — Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync _(★647, JavaScript)_
- [awesome-decision-models](https://github.com/AnotiaWang/awesome-decision-models) — A curated list of decision models (System One / typed decision models): hosted APIs, open-weight models, runtimes, SDKs, applications, benchmarks, and papers. _(★606, Python)_
- [awesome-jev](https://github.com/kydlikebtc/awesome-jev) — 1207 public resources for Jev, TypeSafe AI's System One decision model, indexed by decision pattern. Source citations, dated link checks and scheduled call-site text checks; runtime and performance are not independently tested here. EN/中文,  _(★592, Python)_
- [awesome-jev](https://github.com/AnotiaWang/awesome-jev) — A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources. _(★591, n/a)_
- [awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe-jev) — Awesome Jev: a source-backed field guide to TypeSafe's System One model, with SDKs, live demos, agent tools, and independent evaluations. _(★555, HTML)_
- [awesome-jev](https://github.com/cobanov/awesome-jev) — A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions. _(★496, n/a)_
- [awesome-jev](https://github.com/OmniJev/awesome-jev-gallery) — 🔥🔥 Papers, open reproductions and independent evaluations behind System One models and Jev. _(★488, JavaScript)_
- [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) — Awesome list of TypeSafe AI Jev use cases: 74 demos ranked by likes, 150+ GitHub repos, limits, cost and API examples. CC0 _(★379, n/a)_
- [awesome-jev](https://github.com/Amal-David/awesome-jev) — Jev demos, projects, SDKs and skills, with source links and a curated X gallery. _(★229, Python)_
- [awesome-jev](https://github.com/fatwang2/awesome-jev) — A source-backed Jev project directory with a reusable Jev-only GitHub review workflow. _(★220, JavaScript)_
- [awesome-jev](https://github.com/hellogumbo/awesome-jev) — A community directory of projects built on Jev, TypeSafe AI's System One model. _(★213, JavaScript)_
- [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) — Typed decisions with TypeSafe's Jev, the first System One model _(★188, JavaScript)_
- [awesome-jev](https://github.com/kraayenjon/awesome-jev) — A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities. _(★166, n/a)_
- [awesome-jev](https://github.com/Promethe-us/awesome-jev) — A source-backed Jev / System One knowledge map: projects, papers, evaluations, robotics, and social discovery. _(★136, n/a)_
- [jev](https://github.com/cobusgreyling/Jev) — Unofficial TypeSafe Jev showcase — System One decisions, not chat. _(★131, Python)_
- [awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live) — Awesome Jev — evidence-graded index of TypeSafe System One: SDKs, MCP tools, agents, apps and open models. 20 languages, rebuilt every 2 hours. _(★128, Python)_
- [awesome-jev](https://github.com/AppitStudio/awesome-jev) — Curated Jev resources and runnable examples for typed AI decisions. _(★94, Python)_
- [awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) — Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。 _(★77, HTML)_
- [Awesome-Robot-Use-Agent](https://github.com/visitworld123/Awesome-Robot-Use-Agent) — News: We add many jev+robot in infrastructure. A curated collection of papers and resources on robot-use agents, tool-based robot control, embodied agent runtimes, and self-evolving robotic systems. _(★56, n/a)_
- [awesome-jev](https://github.com/BeatAPI/awesome-jev) — A source-reviewed gallery of JEV-related projects with 50+ GitHub stars — integrations, tools, open models, experiments, and ecosystem resources. Live gallery: beatapi.io/awesome-jev _(★56, JavaScript)_
- [jev-radar](https://github.com/everyinfra/jev-radar) — 📡 全网最全 · The world's most comprehensive tracker of the Jev (TypeSafe AI System One) ecosystem — 220+ documented cases · 108 confidence-graded entries · verified & rescanned every 3 hours · API access guide included _(★31, n/a)_
- [jev-cookbook](https://github.com/nexibeo/jev-cookbook) — Practical, tested recipes for TypeSafe's Jev decision model on OpenRouter: support triage, database indexing, file organizing, tagging, taxonomies, dedupe, PII detection, extraction, search re-ranking and a browser agent. _(★28, JavaScript)_
- [jev-paper-radar](https://github.com/Eliot5566/JEV-Paper-Radar) — Let Jev read every new arXiv paper each morning and surface the few you should read. Plain-English interests, calibrated probabilities, ~$0.06/day, fork and go. _(★27, Python)_
- [jev-hub](https://github.com/mizzlelover/jev-hub) — JEV HUB · X 上关于 TypeSafe AI「系统一模型」Jev 的长文与演示视频聚合（保留原链与作者）｜ 谁是专家 出品 _(★24, CSS)_
- [awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) — Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced. _(★21, n/a)_
- [awesome-jev](https://github.com/tanxarx/awesome-jev) — All things awesome related to Jev _(★21, n/a)_
- [awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) — Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases: repos, patterns, benchmarks, and measured results _(★20, n/a)_
- [awesome-jev](https://github.com/Li-Evan/awesome-jev) — The most complete gallery of what people build with Jev, TypeSafe's System One model: 3,400+ projects, demos, and write-ups by scenario, each with its original link, image, and description. _(★19, HTML)_
- [awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev) — Public examples of Jev used for robot control, 3D modeling and adjacent control tasks, with sources and archived media _(★16, n/a)_
- [jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark) — Reproducible benchmark for measuring Jev reranking quality, latency, and cost in RAG _(★15, Python)_
- [ad-radar](https://github.com/pengchujin/ad-radar) — 开源浏览器插件：在小红书、微博、X、知乎上按关键词和博主折叠内容；用你自己的 Jev API key 识别广告、AI、军事、政治等话题。 _(★15, JavaScript)_
- [awesome-jev](https://github.com/MrJev/awesome-jev) — A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model. _(★15, Python)_
- [awesome-jev-use-cases](https://github.com/whyashthakker/awesome-jev-use-cases) — Awesome list of Jev use cases. Compared with GPT Models (LLMs) across on cost and speed. _(★13, HTML)_
- [awesome-jev](https://github.com/ckaraca/awesome-jev) — A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast, typed decisions. _(★13, Python)_
- [learn-jev-end-to-end](https://github.com/harshithsunku/learn-jev-end-to-end) — Learn Jev end to end: a free hands-on course. Build 13 AI agent use cases with a fast brain (Jev) and a slow brain (LLM). One OpenRouter key. _(★10, Jupyter Notebook)_
- [jevguide](https://github.com/2456868764/jevguide) — Curated Jev showcases from X, organized by category with media previews and direct source links. _(★10, n/a)_
- [awesome-jev](https://github.com/daftAI2026/awesome-jev) — Curated TypeSafe Jev / System One GitHub projects, open-source alternatives, and Jev news _(★10, TypeScript)_
- [jev-usecases](https://github.com/kenhuangus/jev-usecases) — Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic _(★9, Python)_
- [fable-jev](https://github.com/imMamdouhaboammar/fable-jev) — ⚡ Sub-100ms cognitive reflexes for autonomous coding agents. Powered by TypeSafe AI's Jev & get-fable. _(★9, TypeScript)_
- [jevscape](https://github.com/Skyvern-AI/jevscape) — RuneBench harness for TypeSafe's Jev: bounded action catalog, tick-mode controller and a live dashboard _(★8, TypeScript)_
- [awesome-open-system-one](https://github.com/rupeshpoojary9/awesome-open-system-one) — Curated list of the open System One ecosystem: open models, independent benchmarks, calibration and constrained-decoding tooling. _(★8, n/a)_
- [jev-in-the-wild](https://github.com/Jessie-QingYu/jev-in-the-wild) — Real-world Jev use cases, open-source projects, benchmarks and criticism — what people actually build with TypeSafe AI's Jev, and where it fails. Machine-readable, updated daily. _(★7, JavaScript)_
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) — LlamaIndex reranker + router powered by TypeSafe Jev - typed scores/choices, cheaper than LLM-as-judge. _(★6, Python)_
- [awesome-jev](https://github.com/onmyway133/awesome-jev) — Awesome projects built with Jev from Typesafe AI _(★6, n/a)_
- [jev-sap-commerce](https://github.com/Emenowicz/jev-sap-commerce) — SAP Commerce extension using TypeSafe's Jev to moderate product reviews and suggest product categories and classification attribute values: dry runs on your own data first, an audit record per decision. Plus a Claude Code skill. _(★5, Java)_
- [awesome-jev](https://github.com/jtnkminimal/awesome-jev) — A curated projects built with Jev, TypeSafe's System One model. _(★5, Python)_
- *37 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

### More Projects (267)

- [jevlike](https://github.com/vinnylarouge/jevlike) —  _(★1341, Python)_
- [shapeshift](https://github.com/anishfn/shapeshift) — An input that becomes what you mean: one text box that morphs into the right UI as you type. Powered by TypeSafe Jev, works offline. _(★790, TypeScript)_
- [Jev-cu](https://github.com/Sac-Y/Jev-cu) —  _(★614, JavaScript)_
- [mobile-jev](https://github.com/droidrun/mobile-jev) —  _(★431, JavaScript)_
- [jev-experiments](https://github.com/dabit3/jev-experiments) —  _(★396, TypeScript)_
- [jev-visual](https://github.com/hr98w/jev-visual) — An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos. _(★304, Python)_
- [crush-monitor](https://github.com/FerryCorleone/crush-monitor) — Crush 好感监控器：用 Jev 分析微信聊天的情绪、意图和回复表现。本机部署，使用自己的 API Key。 _(★268, TypeScript)_
- [djev-spark](https://github.com/mmastrac/djev-spark) — DiffusionGemma NVFP4 structured decisions on a DGX Spark: container recipe _(★197, HTML)_
- [jevify](https://github.com/ryana/jevify) — Prompts to jev-ify your projects _(★193, n/a)_
- [Jevmind](https://github.com/dealerdefi/Jevmind) —  _(★183, Python)_
- [Jev-X-Sentiment-Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) —  _(★174, Python)_
- [jevbox](https://github.com/extend-hq/jevbox) —  _(★140, TypeScript)_
- [jev-cookbook](https://github.com/datawhalechina/jev-cookbook) — Jev 模型（TypeSafe AI）官方使用文档的中文翻译 | Unofficial Chinese translation of the official Jev (TypeSafe AI) docs — https://docs.typesafe.ai _(★128, Python)_
- [typesafe_register](https://github.com/Futureppo/typesafe_register) — typesafe.ai注册机，极致优化，无限jev _(★125, Python)_
- [jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension) — A small extension that demos the combination of Jev x WebMCP _(★124, JavaScript)_
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) — Fish-style zsh history autosuggestions ranked by Jev (TypeSafe) _(★112, TypeScript)_
- [MedJev](https://github.com/JunMa11/MedJev) —  _(★109, Python)_
- [jev-leftpad](https://github.com/f/jev-leftpad) — Left-pad strings with TypeSafe AI's Jev. For reasons. _(★85, JavaScript)_
- [jevcache](https://github.com/hyperspaceai/jevcache) — A decision cache for TypeSafe Jev-class models — memoize decisions so repeats are free, deterministic, and shareable. One 2 MB binary. _(★75, n/a)_
- [jev-case](https://github.com/Hiwoniu/Jev-Case) — 收集全网优秀 case 的收藏库 | A curated collection of excellent cases from across the web _(★66, TypeScript)_
- [jevix](https://github.com/ur001/Jevix) — Средство для фильтрации HTML и автоматического типографирования _(★66, PHP)_
- [dspy-typesafeify](https://github.com/typesafeainate/dspy-typesafeify) — Add a decorator for dspy Signatures that automatically uses TypeSafe where relevant _(★63, Python)_
- [mini-jev](https://github.com/r-ms/mini-jev) — mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench. _(★55, Python)_
- [robojev](https://github.com/lykycy123/RoboJEV) — Two-stage JEV control of a Franka Panda in MuJoCo _(★49, Python)_
- [jevoisbase](https://github.com/jevois/jevoisbase) — JeVois base collection of algorithms and modules _(★48, C)_
- [vibecheck](https://github.com/RafalWilinski/vibecheck) — Chrome extension: vibe-check your X posts with TypeSafe's Jev before you hit Post _(★47, JavaScript)_
- [litjev](https://github.com/zhengxuyu/litjev) — Turn any off-the-shelf LLM into a Jev -like decision layer _(★44, Python)_
- [call-coach-ai](https://github.com/ZeroGold/call-coach-ai) — Jev powered call coach _(★43, HTML)_
- [pijev](https://github.com/TypeLLM/pijev) — Permutation Invariant Jev _(★35, Python)_
- [jev_apps](https://github.com/JackZeng/Jev_apps) — 看看 Jev 能做什么：用中英文讲清热门应用、工作原理和各自优缺点。Explore Jev apps with plain-language examples, explanations, and comparisons. _(★34, Python)_
- [is-jeven](https://github.com/wobsoriano/is-jeven) — Is it even? Ask Jev. _(★33, JavaScript)_
- [jev-explained](https://github.com/davila7/jev-explained) — Jev Explained _(★31, TypeScript)_
- [mojev](https://github.com/MoLeMo-Lab/mojev) — MoJev: typed, calibrated decisions in one forward pass. _(★30, Python)_
- [minojev](https://github.com/zeredy879/minojev) — Decisions, not tokens: minojev reads calibrated, typed probability distributions straight from hidden states in one forward pass — zero output tokens, fully reproducible on a laptop CPU. _(★25, Python)_
- [jev-reranker](https://github.com/hotchpotch/jev-reranker) — Jev-powered relevance filtering and reranking for RAG in Python. _(★24, Python)_
- [hookmeter-jev](https://github.com/ehui1226/hookmeter-jev) — ⚡ Millisecond-level Viral Hook Telemetry & Co-pilot for Social Media (Chrome Extension + JEV System 1) _(★22, HTML)_
- [invalidate](https://github.com/chopratejas/invalidate) — The invalidation layer for AI memory. Every fact gets a lease; new evidence ends it. Built on TypeSafe Jev. _(★21, Python)_
- [pix-golpe](https://github.com/sandeco/pix-golpe) — Demo: IA detecta golpe do Pix e rastreia a quadrilha. Rust + Jev vs Python + DeepSeek em tela dividida. _(★19, Python)_
- [jev-cpu](https://github.com/leesk212/JEV-CPU) — Run SemIf (Jev-style semantic-if decisions) on a CPU — no GPU. Reads typed option probabilities straight from an open model in one forward pass, plus a web UI. _(★19, Python)_
- [x-scanner](https://github.com/oso95/x-scanner) — Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter _(★18, TypeScript)_
- [Jev](https://github.com/mayank953/Jev) —  _(★18, JavaScript)_
- [jev-to-answer](https://github.com/csskrtao/jev-to-answer) — 答案之书jev _(★17, JavaScript)_
- [hunch](https://github.com/carldaws/hunch) — Probabilistic control flow for Ruby and Rails - powered by TypeSafe's Jev _(★16, Ruby)_
- [jev-me](https://github.com/jon-devlapaz/jev-me) — Grill-me with Jev optional each turn _(★14, n/a)_
- [typesafe-ai](https://github.com/Twister915/typesafe-ai) — Typed TypeSafe AI clients for Rust, with async and blocking backends and observable retries. _(★13, Rust)_
- [super-jev](https://github.com/Kevthetech143/super-jev) — A small, extensible decision-to-action harness for TypeSafe Jev _(★13, Python)_
- [pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) — Pi extension: verbatim context compaction with TypeSafe Jev decisions _(★12, TypeScript)_
- [xtags](https://github.com/manifoldor/xtags) — 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型。 _(★12, JavaScript)_
- [gut](https://github.com/vinibrsl/gut) — Use LLM judgment in regular Elixir control flow. _(★12, Elixir)_
- [jev-tree](https://github.com/reachjalil/jev-tree) — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap. _(★9, TypeScript)_
- *217 more — see the [full browsable catalog](https://therocksss.github.io/awesome-jev/)*

<!-- PROJECTS:END -->

## Quality standard

An entry must:

1. **Actually use, implement, or integrate Jev / System One** — or be official TypeSafe tooling.
2. Be a **public GitHub repository** (archived repos stay, tagged via the page).
3. Show a clear Jev / TypeSafe System One connection in the repository name, description, official ownership, or homepage. New zero-star projects can qualify; topics alone do not establish relevance.
4. Be described by its real GitHub description — no marketing copy.

## How this list updates

[`scripts/update_list.py`](scripts/update_list.py) runs every day via GitHub Actions: it searches GitHub for new Jev/TypeSafe repos, verifies each one, refreshes star counts, and stamps `added` dates. Newest additions appear at the top of the page under **🆕 Added today**. See [docs/DATA.md](docs/DATA.md) for the dataset schema and provenance.

## Contributing

Missing a project? Open an issue or PR — see [CONTRIBUTING.md](CONTRIBUTING.md). Additions must meet the quality standard above.

## Provenance & credit

This catalog merges and deduplicates **20+ community awesome lists** (see [docs/AWESOME_LISTS.md](docs/AWESOME_LISTS.md)) plus direct GitHub discovery of the `typesafe-ai` org and `jev`/`typesafe` repos. All project content belongs to its authors; TypeSafe, Jev, and System One are trademarks of their respective owners and this catalog is **not affiliated with or endorsed by TypeSafe**.

## License

[CC0-1.0](LICENSE) — the catalog text is public domain; linked code keeps its own license.
