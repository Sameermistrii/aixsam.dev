"""Long-form content for every setup guide: "What is it", "What it can do" and an FAQ.
Facts come from each tool's own README (checked 2026-10-24). Edit the text here, then run:
    python3 tools/extra.py && python3 tools/seo.py
Re-runnable: the blocks between <!--x:about--> / <!--x:faq--> markers are replaced, not duplicated."""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
REELS = {'clone': 'https://www.instagram.com/reel/Deg1itXTSUr/', 'graph': 'https://www.instagram.com/reel/DeivnmwTSTG/'}

C = {}
C['replica'] = dict(
    about=["<b>Replica</b> is a set of eleven free Claude skills by Jake Schincariol that help you clone an app: study it, rebuild it, test it and launch your own version. It's MIT licensed, needs no signup and no API key, and connects to nothing.",
           "What makes it different is the order. One skill maps the app you want to study, the next ones plan, design, build and test your version, and one of them, the <b>Entrepreneur</b>, reads what the original app's users complain about so your version fixes it. Every skill writes into a <code>replica/</code> folder that the next one reads.",
           "It copies what an app <b>does</b>, its features and flows, never what it <b>owns</b>: no code, logo, copy or content. The brand and sweep tools check for that before you launch."],
    can=[("/replica-recon", "maps an app's screens, flows, components and data model from public pages, screenshots, store listings and your own account."),
         ("/replica-architect", "plans the stack, database schema and API."),
         ("/replica-design", "rebuilds the design system as tokens: colours, type, spacing, components, with your own assets."),
         ("/replica-build and /replica-backend", "build the app screen by screen, then add sign-in, database, payments and integrations."),
         ("/replica-test and /replica-diff", "click through every flow looking for bugs, then score your clone against the original and list what's missing."),
         ("/replica-entrepreneur", "reads real reviews (every quote it shows links to its source) and turns the top complaints into fixes and a positioning angle."),
         ("/replica-brand, /replica-launch, /replica-deploy", "give it a new name and look, write the landing page and store listing, and put it live on your domain.")],
    faq=[("Is Replica skill free?", "Yes. It's open source under the MIT licence, with no signup and no API key. You only need Claude."),
         ("Is it legal to clone an app with it?", "Replica is built to copy features and flows, clean-room style, not code, logos, text or content, and its brand and sweep tools check that nothing of the original is left. Laws differ by country, so check with a lawyer before you sell a clone of a well-known product."),
         ("Do I need Claude Code?", "No. Claude Code gets all eleven skills plus the Python helper tools. In any other Claude chat you can paste a single <code>SKILL.md</code> at the top and it works as a mode, just without the tools."),
         ("Can I run only one of the skills?", "Yes. Each skill works on its own. Running <code>/replica-entrepreneur</code> on an app you're only thinking about cloning is a quick way to find out if it's worth it."),
         ("What do the Python tools need?", "Python 3.8 or newer. They use only the standard library, so there's nothing to pip install, and none of them touch the network.")])

C['graphify'] = dict(
    about=["<b>Graphify</b> is a free, open-source tool that reads a folder (your code, notes, PDFs, screenshots, diagrams) and builds a <b>knowledge graph</b> of how everything connects. Your AI coding assistant can then ask the graph instead of opening and re-reading every file in each new session.",
           "Code is parsed locally with tree-sitter, so it never needs an AI to understand your functions and imports. Docs, papers and images are read by Claude to pull out concepts and links. Every connection in the graph is marked as <i>extracted</i>, <i>inferred</i> or <i>ambiguous</i>, so you can see what was found and what was guessed.",
           "How much it saves depends on size. On the project's own benchmark of 52 files (3 repos, 5 papers, 4 images) a query used <b>71.5× fewer tokens</b> than reading the raw files; on 4 files it was 5.4×, and on 6 small files about the same as reading them. The bigger the folder, the bigger the win."],
    can=[("An interactive map", "<code>graph.html</code>: click, search and filter your code by community."),
         ("A one-page report", "<code>GRAPH_REPORT.md</code> lists the &quot;god nodes&quot; everything runs through, surprising connections, and questions the graph can answer."),
         ("Questions in plain English", "<code>/graphify query</code>, <code>path</code> and <code>explain</code> answer from the graph."),
         ("Stays up to date", "<code>--update</code> re-reads only changed files; <code>--watch</code> or a git commit hook rebuilds it automatically."),
         ("Exports", "an Obsidian vault, a wiki for agents, SVG, GraphML (Gephi, yEd), Neo4j, or an MCP server."),
         ("Any mix of files", "Python, TypeScript, Go, Rust, Java, C/C++ and more, plus Markdown, PDFs and images.")],
    faq=[("Is Graphify free?", "Yes, it's free and open source. Building the graph from code costs nothing; reading docs, PDFs and images goes through your AI assistant, like any other request."),
         ("Why is the package called graphifyy?", "The PyPI name <code>graphify</code> is being reclaimed, so the official package is temporarily <code>graphifyy</code> (two y's). The command you type is still <code>graphify</code>."),
         ("Does it work with Cursor or Codex, not just Claude Code?", "Yes. <code>graphify install</code> sets up Claude Code, and there are install options for Cursor, Codex and other assistants (step 3 above)."),
         ("“graphify” is not recognized on Windows", "Add Python's Scripts folder to your PATH (<code>%APPDATA%\\Python\\Python3xx\\Scripts</code>), or install with uv or pipx, which handle the PATH for you."),
         ("Will it really save 71.5× tokens on my project?", "Only on a big, mixed folder like the benchmark's 52 files. Small projects that already fit in the context window save little; there the value is seeing the structure, not saving tokens.")])

C['voicebox'] = dict(
    about=["<b>Voicebox</b> is a free, open-source AI voice studio by Jamie Pine that runs on your own computer. It does the job of a voice-cloning service and a dictation app in one: clone a voice from a few seconds of audio, turn text into speech, and dictate into any app with a hotkey.",
           "Everything stays on your machine: the models, your voice samples and your recordings never leave it. It's built with Tauri (Rust), not Electron, and runs on Apple Silicon (MLX/Metal), Windows (CUDA), AMD and Intel graphics, or Docker.",
           "It includes eight speech engines you can switch between per generation, and an MCP server, so AI agents like Claude Code can talk back to you in a voice you made."],
    can=[("Clone a voice", "zero-shot from a short sample, or pick from 50+ preset voices."),
         ("23 languages", "from English to Hindi, Arabic, Japanese and Swahili; which ones you get depends on the engine you pick."),
         ("Long scripts", "auto-chunking with crossfades for articles, chapters and full scripts."),
         ("Stories editor", "a multi-track timeline for podcasts, conversations and narration."),
         ("Expressive speech", "tags like [laugh] and [sigh] with Chatterbox Turbo, or describe a voice in words with Qwen VoiceDesign."),
         ("Dictation", "a global push-to-talk hotkey that types what you say into any text field (Whisper-based)."),
         ("Effects and API", "pitch, reverb, compression and more; a REST API and MCP server for your own apps and agents.")],
    faq=[("Is Voicebox free?", "Yes. It's MIT licensed and the app has no splash screens, banners or paid tiers."),
         ("Is my voice uploaded anywhere?", "No. Models, voice data and recordings stay on your computer."),
         ("Does it speak Hindi?", "Yes, Hindi is one of its 23 languages. Support differs between the eight engines, so if one engine doesn't offer it, switch to another."),
         ("Do I need a graphics card?", "It's faster with one (Apple Silicon, NVIDIA, AMD or Intel), but the light LuxTTS engine runs about 150× faster than real time on an ordinary CPU, in English."),
         ("Is there a Linux version?", "Not as a download yet. On Linux you build it from source (voicebox.sh/linux-install) or run it with Docker."),
         ("Can I clone anyone's voice?", "Only clone your own voice or someone who has said yes. Cloning other people's voices without permission can be illegal and is always unfair to them.")])

C['ecc'] = dict(
    about=["<b>ECC (Everything Claude Code)</b> is a free, MIT-licensed add-on (github.com/affaan-m/ECC) that gives your AI coding agent a whole engineering process instead of one helper: it plans before it builds, writes tests, reviews its own work from a fresh context, remembers what matters, and turns repeated wins into reusable skills.",
           "The loop it follows is <b>plan → test → implement → review → verify → remember → improve</b>, so you don't have to type that process into every prompt.",
           "It works best with Claude Code, has native Codex and Qoder plugins, and lighter adapters for Cursor, OpenCode, Gemini, Zed, GitHub Copilot and others (not every feature works everywhere)."],
    can=[("71 agents", "specialists for planning, code review, build repair, security and more."),
         ("311 skills", "focused how-tos (like the TDD workflow) that load only when needed, so your context stays small."),
         ("Hooks and rules", "automatic checks and project rules that run while the agent works."),
         ("Memory", "shares context between sessions and even between different agents."),
         ("AgentShield", "security scanning for the agent setup itself."),
         ("97 legacy commands", "the older slash commands, kept working while you move to skills.")],
    faq=[("Is ECC free?", "Yes. The repo is MIT licensed and stays free. ECC Pro is a separate paid GitHub App for private repos; you don't need it to use ECC."),
         ("Where should I install it from?", "Only from official sources: github.com/affaan-m/ECC, the npm packages <code>ecc-universal</code> and <code>ecc-agentshield</code>, the plugin <code>ecc@ecc</code>, or ecc.tools. The project warns that re-uploads and mirrors may contain malware."),
         ("Which install should I pick?", "One only: the guided <code>npx</code> setup or the <code>/plugin</code> commands. Both install the same plugin, and stacking them causes conflicts."),
         ("It fills up my context. Can I make it lighter?", "Yes. The README has a low-context, no-hooks install path, and you can install just the agents or just some skills."),
         ("Does it work with Cursor or Codex?", "Codex has a native plugin. Cursor and other editors get a reduced adapter, so check the support table in the README before relying on a feature.")])

C['linkedin-skills'] = dict(
    about=["<b>LinkedIn Skills</b> is a free, MIT-licensed bundle of 12 Claude skills by Serge Bulaev that write your LinkedIn posts, comments and replies in your own voice. They draft, strip the typical AI tells, and wait for your approval: nothing is published unless you say so.",
           "You don't need to code. On claude.ai or Claude Desktop you add it as a plugin in a few clicks; it also works in Claude Code, the Codex CLI and other agents that read SKILL.md files. The right skill switches on by itself when you mention LinkedIn."],
    can=[("Post Writer", "drafts posts from 20 hook formulas, picked by what you want the post to achieve."),
         ("Comment Drafter and Reply Handler", "draft a comment from any post URL, or sweep a whole thread and draft replies in one batch."),
         ("Post Audit and Humanizer", "check a draft against platform rules and AI patterns, and remove the phrases readers recognise as AI."),
         ("Hook Extractor", "turns any viral post into a blank template for your own topic."),
         ("Content Planner", "a 7-day plan with topics, formats, hooks and posting times."),
         ("Profile Optimizer", "rewrites your headline, About, Featured and Experience sections."),
         ("Interviewer, Repurposer, Engagement Monitor, Employee Advocacy", "build a story bank from your career, turn tweets or videos into LinkedIn posts, track replies, and plan a team posting program.")],
    faq=[("Is it free?", "The skills are free and MIT licensed. You need a paid Claude plan (Pro, Max, Team or Enterprise) with code execution turned on, or Claude Code."),
         ("Will it post to LinkedIn by itself?", "No. It only writes drafts. Auto-posting is an optional extra through a third-party service (Publora) that you'd have to connect yourself."),
         ("Will its posts pass AI detectors?", "The authors are honest about this: the humanizer removes common AI tells but doesn't promise to beat detectors, because no edit reliably does. It even shows how much the detectors disagree with each other."),
         ("I synced the marketplace but can't find the skills", "Syncing only adds the plugin to <b>Discover</b>. Press the <b>+</b> on the plugin card, then check it's listed under <b>Yours</b>."),
         ("Cloning on Windows loads no skills", "The repo uses symlinks, which Windows only creates with Developer Mode or <code>git config core.symlinks true</code>. Use the plugin install instead, or the junction command in the README.")])

C['moneyturbo'] = dict(
    about=["<b>MoneyPrinterTurbo</b> is a free, open-source (MIT) app by harry0703 that turns one topic or keyword into a finished short video. It writes the script with an AI model, finds matching stock footage, adds a voiceover, syncs subtitles, adds background music and renders the video, while letting you change any step.",
           "It runs on Windows, Mac or Linux without a graphics card, because it edits stock clips instead of generating video. You can use it through a web page in your browser, an API, a command line or an AI agent.",
           "Despite the name, it doesn't make money by itself: it makes videos fast. What you do with them is up to you."],
    can=[("Topic to video", "script, voice, footage, subtitles and music in one go, or bring your own script."),
         ("Many AI models", "OpenAI, Claude, Gemini, DeepSeek, Qwen, Grok and more for the script, or Ollama for a free model on your own PC."),
         ("Free footage and voice", "stock clips from Pexels and Pixabay, and Edge TTS voices that need no key."),
         ("Your own material", "upload your own images and videos, or plug in AI video generators if you have a key."),
         ("Subtitles your way", "font, position, colour, size, outline and background."),
         ("Every format", "9:16 (1080×1920), 16:9 (1920×1080) or 1:1 (1080×1080), and batches of several versions at once.")],
    faq=[("Is MoneyPrinterTurbo free?", "The app is free and MIT licensed. Pexels footage and Edge TTS voices are free too. The AI that writes the script may cost a little, unless you use a free local model with Ollama."),
         ("Do I need a graphics card?", "No. It edits stock footage, so an ordinary computer with 4 GB of RAM works (8 GB is better)."),
         ("Which pip package is the real one?", "<code>mpt</code>. A package named &quot;MoneyPrinterTurbo&quot; on PyPI is made by someone else, so don't install that one."),
         ("Can it make videos in Hindi?", "It can write multilingual scripts, and Edge TTS has Hindi voices. Pick a Hindi voice in the voice settings and check the subtitle font shows Hindi correctly."),
         ("Can I post the videos as my own?", "The footage comes from free stock libraries, so check each library's licence, and add your own angle. Plain stock-clip videos tend to perform worse than ones with a real point of view.")])

C['dev-team'] = dict(
    about=["This guide sets up <b>five free tools</b> that turn Claude Code from a single coder into something closer to a small team: a planner that slows it down before it writes code, a researcher that pulls current library docs, a reviewer, a cleaner, and a leadership crew of specialist reviews.",
           "<b>Superpowers</b> (by Jesse Vincent) makes Claude ask what you're really building, write a spec you approve in short chunks, then a plan of small tasks it builds test-first. <b>Context7</b> (by Upstash) fetches up-to-date, version-specific documentation so Claude stops inventing APIs that don't exist. <b>/code-review</b> and <b>/simplify</b> are built into Claude Code. <b>gstack</b>, by Y Combinator's Garry Tan, adds 23 specialist roles, from a CEO-style plan review to a QA lead that tests in a real browser.",
           "Add them one at a time and try each before adding the next, so you know what each one changes."],
    can=[("Plan first", "Superpowers turns a vague idea into a spec and a step-by-step plan before any code is written."),
         ("Build test-first", "Superpowers' plans follow red/green TDD, YAGNI and DRY, and can run for hours without drifting from the plan."),
         ("Current docs", "add <code>use context7</code> to a prompt and Claude reads today's docs for your libraries."),
         ("Catch bugs", "<code>/code-review</code> checks a change before your users find the problems."),
         ("Clean up", "<code>/simplify</code> removes complexity Claude added along the way."),
         ("Specialist reviews", "gstack's <code>/plan-ceo-review</code>, <code>/review</code>, <code>/qa</code>, <code>/cso</code> and more.")],
    faq=[("Are all five really free?", "Yes. Superpowers and gstack are free and open source, /code-review and /simplify come with Claude Code, and Context7 has a free tier (a free key from context7.com raises the limits). You still need Claude Code itself on a Claude plan."),
         ("Do I need all five?", "No. Start with Superpowers. Add Context7 if Claude keeps getting library code wrong, and gstack when you want deeper reviews and browser testing."),
         ("Does gstack work on Windows?", "Yes, through Git Bash or WSL: run <code>.\\setup.ps1</code> in PowerShell from the gstack folder. If Windows 11's Smart App Control blocks its browser tool, the other gstack skills still work."),
         ("Will these slow Claude down or use more tokens?", "Planning and reviews do add steps, and that's the point: they catch mistakes that would cost more to fix later. Install one at a time so you can feel the difference.")])

C['browser-use'] = dict(
    about=["<b>browser-use</b> is a free, open-source (MIT) library that gives an AI model a real web browser. You describe a task in one line, like &quot;find the cheapest flight to Goa next Friday&quot;, and the agent opens sites, reads them, clicks, types and fills in forms by itself.",
           "You can run it entirely on your own computer from Python, with any AI model, including a free local one through Ollama. The same team also sells an optional cloud service with hosted browsers; you don't need it for anything in this guide.",
           "There are three ways in: a Python library (this guide), a command-line tool that plugs into agents like Claude Code, or their hosted cloud."],
    can=[("Do web tasks for you", "search, compare, fill forms, collect information across several sites."),
         ("Any model", "OpenAI, Claude, Gemini, or a free local model with Ollama."),
         ("Your code, your browser", "it's a normal Python library (Python 3.11+), so you can build it into your own scripts."),
         ("Works with coding agents", "the CLI path registers a skill so Claude Code or Codex can drive a browser.")],
    faq=[("Is browser-use free?", "The library is free and MIT licensed. You pay only for the AI model if you use a paid one; Ollama models are free. The cloud browsers are a separate, optional paid service."),
         ("Is it safe to let an AI control my browser?", "Treat it like giving someone your mouse. Use a separate browser profile, don't let it log in to your bank or email, and watch what it does the first few times."),
         ("Can it solve CAPTCHAs?", "The paid cloud browsers advertise CAPTCHA handling. Running locally, expect it to stop at CAPTCHAs, and respect each site's rules."),
         ("Which model works best?", "Bigger models follow multi-step tasks better. Small local models are free and private but slower and make more mistakes on long tasks.")])

C['content'] = dict(
    about=["This guide covers <b>three free, open-source tools</b> that together replace a voice artist, a designer and a video editor: <b>GPT-SoVITS</b> speaks in your voice, <b>ComfyUI</b> makes images and AI video on your own computer, and <b>OpenCut</b> edits everything together.",
           "<b>GPT-SoVITS</b> (by RVC-Boss) clones a voice from about 5 seconds of audio, and gets closer with about 1 minute of training audio. <b>ComfyUI</b> is a visual node editor for image, video, audio and 3D models that runs locally. <b>OpenCut</b> is a free, MIT-licensed video editor; it's being rewritten from scratch, and opencut.app runs the classic version you can use today.",
           "Set them up one at a time. They don't depend on each other."],
    can=[("Your voice from 5 seconds", "GPT-SoVITS zero-shot voice cloning, or fine-tune on 1 minute of audio for better likeness."),
         ("Built-in helpers", "GPT-SoVITS includes tools to separate voice from music, cut training clips and label text."),
         ("Images and video, offline", "ComfyUI runs models like Flux, SDXL, Wan and LTX-Video on your own graphics card."),
         ("Reusable workflows", "ComfyUI's templates, subgraphs and local API let you save a workflow and reuse it."),
         ("Free editing", "OpenCut in the browser at opencut.app, free and open source.")],
    faq=[("Can GPT-SoVITS speak Hindi?", "Not yet. It supports English, Japanese, Korean, Cantonese and Chinese, and can speak a different one of those than the language you trained it on."),
         ("Do I need a graphics card?", "For ComfyUI's video models, yes, a good one (NVIDIA, AMD, Intel or Apple Silicon). GPT-SoVITS is fast on a modern NVIDIA card and works slower on a CPU. OpenCut runs in the browser."),
         ("Is OpenCut ready to use?", "The classic version at opencut.app is usable today. The project is being rebuilt with desktop, mobile and an editor API, so expect changes."),
         ("Can I clone someone else's voice?", "Only your own, or someone who has agreed. Cloning a voice without permission can be illegal."),
         ("Are they really free?", "Yes, all three are free and open source. ComfyUI and its local models cost nothing; you only need the hardware to run them.")])

C['claude-code-free'] = dict(
    about=["<b>Claude Code</b> is an AI coding agent: it reads your files, edits code and runs commands in your terminal. The agent and the model are separate pieces. By default it uses Claude as its brain, but it can talk to other models through <b>OpenRouter</b>, including free ones like Google's Gemma or NVIDIA's Nemotron.",
           "That's what this guide sets up: the Claude Code agent with a free model behind it, so you can try agentic coding without a paid plan. Be clear about the trade-off: you get Claude Code's tools and workflow, not Claude's intelligence, and free models are weaker and rate-limited."],
    can=[("Real agent workflow", "Claude Code reads your project, edits files and runs commands, just with a different model."),
         ("No card needed", "OpenRouter's free models work on a free account."),
         ("Switch models anytime", "change one setting to try a different free model, or a paid one later.")],
    faq=[("Is this really free?", "The models marked <code>:free</code> on OpenRouter cost nothing, but they have daily request limits. Check OpenRouter's limits page for the current numbers."),
         ("Is it as good as Claude?", "No. You get Claude Code, the agent, not Claude, the model. Free models make more mistakes, especially on long or tricky tasks."),
         ("Will it ever charge my Claude subscription?", "Not with the settings in this guide: every model slot points to the free OpenRouter model, so nothing falls back to a paid Claude model. Run <code>/status</code> to check what it's using."),
         ("Is my OpenRouter key safe?", "Treat it like a password: never paste it in a comment, a screenshot or a video. If it leaks, delete it in OpenRouter and make a new one."),
         ("OpenRouter says it isn't guaranteed to work", "Right: Anthropic only guarantees Claude Code with its own models. Most things work with other models, but some features may not.")])

C['instagram-agent'] = dict(
    about=["<b>Instagram Agent Skill</b> is a free, MIT-licensed set of 13 Claude skills by Jake Schincariol that help you run an Instagram account: write Reels from 26 hook formulas, find what's working in your niche, write captions, plan the week and score your profile.",
           "It needs no Instagram login and no API key, and it never posts, comments or DMs for you. It writes drafts; you post. Every skill reads a short <code>voice.md</code> file about how you talk, so spend ten minutes filling it in first."],
    can=[("/ig-reel", "turns one idea into three scored hooks, a script, on-screen text and a timed beat sheet."),
         ("/ig-viral", "finds reels that beat their own account's usual numbers in your niche and names the formula."),
         ("/ig-caption", "writes the caption and shows exactly what fits before the &quot;… more&quot;."),
         ("/ig-carousel and /ig-story", "swipe-post copy and files, and a daily story sequence."),
         ("/ig-profile", "scores your profile out of 100 on a 12-part rubric and rewrites what lost points."),
         ("/ig-plan", "the week: what to post, which format, when, and accounts to engage with."),
         ("/ig-human", "the humanizer: strips em dashes, AI vocabulary and hidden watermark characters, then checks the draft.")],
    faq=[("Does it need my Instagram password?", "No. It never logs in to Instagram and never posts, comments or DMs. You copy the drafts and post them yourself."),
         ("Is it free?", "Yes, MIT licensed. You need Claude with skills (a paid plan with code execution) or Claude Code."),
         ("What is voice.md?", "A short file describing how you talk. Every skill reads it, which is why the drafts sound like you. You can ask Claude to write it from three of your reels."),
         ("Does it work without Claude Code?", "Paste a single <code>SKILL.md</code> into a chat and it works as a mode, but you lose the Python tools that score hooks and run the humanizer.")])

C['pipeline'] = dict(
    about=[],
    can=[],
    faq=[("Do I need ElevenLabs?", "No. Any voice works: your own recording, a free text-to-speech voice, or ElevenLabs. The starter kit was tested end to end with a free Piper voice."),
         ("Do I need a graphics card?", "No. The reel is a web page that a headless browser screenshots frame by frame, and ffmpeg joins the frames. A normal laptop is enough."),
         ("How long does a render take?", "My 40–60 second reels render in about 3 minutes, split into three parts that run at the same time."),
         ("Does it work for Hindi or Hinglish?", "Yes. The kit's aligner handles Hinglish written in English letters, which is how I make my Hinglish reels.")])


C['freellmapi'] = dict(
    about=["<b>FreeLLMAPI</b> is a free, open-source (MIT) app by Tashfeen Ahmed that collects the free plans of 34 AI providers (Google Gemini, Groq, Mistral, OpenRouter, Cerebras and more) and puts them behind <b>one</b> OpenAI-compatible key that runs on your own computer.",
           "On its own, each free plan is small: a few million tokens a month or a few thousand requests a day. Stacked together, the README puts them at roughly <b>7.4 billion tokens a month</b> across 635 free model endpoints, if you add every provider. Your app sends a request to one address, and the router picks a free model that still has room; on a rate limit it moves to the next one by itself.",
           "Your provider keys are stored encrypted on your machine, and your apps only ever see a single <code>freellmapi-</code> key. The core app is free; an optional $19/year premium only gets new models into the catalog sooner."],
    can=[("One key for many AIs", "add free keys from as many providers as you like; your apps use one."),
         ("Auto switch", "a model hits its free limit (a 429 error), and it retries the next model in your chain."),
         ("Works with your apps", "anything that takes an OpenAI base URL, plus Claude Code, Cursor, Cline, Codex CLI and Aider."),
         ("Dashboard", "manage keys, drag the fallback order, try prompts in a playground and see your monthly token budget."),
         ("Desktop app", "Mac and Windows, lives in the tray, no account or password to set up."),
         ("More than chat", "embeddings, images and speech go through the same key where a free provider offers them.")],
    faq=[("Is FreeLLMAPI really free?", "The app is free and MIT licensed, and the tokens come from each provider's own free plan. A $19/year premium is optional; it only gets new models sooner (free installs get them about 30 days later)."),
         ("Do I get GPT-4 or Claude for free?", "No. The newest paid GPT and Claude models aren't among the free providers. You get open and fast models like Gemini, Llama, Qwen, DeepSeek and Mistral. Claude Code can still run on top of your free pool."),
         ("Will I really get 7.4 billion tokens?", "Only if you add a key from every provider. Start with 2 or 3 and you'll have less; each provider's limits can also change without notice."),
         ("Can I use it for my business?", "The project says it's for personal experimentation and learning, not production. Free plans have no guarantee, and each provider's terms still apply. Swap in a paid API before you ship anything real."),
         ("Are my keys safe?", "They stay on your computer, encrypted, and are decrypted only in memory per request. Never paste them in a video, screenshot or public file.")])


C['cleanyourtv'] = dict(
    about=["<b>CleanYourTV</b> is a free, open-source (MIT) project by GitHub user Gathin23 that cleans up Android TV and Google TV sets over Wi-Fi. It switches off the maker's ad services, sponsored rows, tracking and preloaded junk apps, then installs a small home screen that looks like an Apple TV's.",
           "It started when the author's parents' Mi TV showed an ad before they could reach Netflix. He cleaned it with Claude Code, posted the before and after, and within days people had added their own TVs: the README lists <b>316 tested models from 89 brands</b>. It was the #1 trending repo on GitHub for the week of 19–25 October 2026.",
           "Apps are switched off with Android's own <code>pm disable-user</code>, never uninstalled, and a backup is made first, so <b>one command puts everything back</b>. No root, no cable, and the firmware isn't touched."],
    can=[("Switch off the ads", "the ad services, sponsored rows and \"Discover\" nags on the home screen."),
         ("Cut the tracking", "analytics and telemetry apps that phone home, and preloaded apps you never asked for."),
         ("A new home screen", "a pitch-black, Apple TV-style home with a dock of your 4 favourite apps and the rest in a grid."),
         ("Keep the useful bits", "Inputs (HDMI), Wi-Fi and Settings buttons, a clock screensaver, and the remote's Input and YouTube buttons."),
         ("Ask before it touches anything", "the agent checks which apps you use, and whether to keep the voice assistant, Chromecast and updates."),
         ("Undo in one line", "<code>tools/restore.sh</code> switches back on exactly what was switched off and brings the old home screen back.")],
    faq=[("Is CleanYourTV free?", "Yes. It's open source under the MIT licence. The laptop way needs an AI coding agent such as Claude Code, which may need its own plan; the phone app is free."),
         ("Does it work on Samsung or LG TVs?", "No. Samsung uses Tizen and LG uses webOS, not Android. It works on Android TV and Google TV sets, and partly on Amazon Fire TV (ads and tracking off, but no new home screen)."),
         ("Does it remove YouTube ads?", "No. It cleans the TV's own home screen and system apps. Ads inside apps like YouTube come from the app itself and stay."),
         ("Can it break my TV?", "Nothing is flashed, rooted or deleted, so the firmware is safe. The risk is switching off something the TV needs, which can get it stuck. Go in small batches, keep the backup, and the TV's Settings → Apps page can switch apps back on. A factory reset is the last resort."),
         ("Is leaving USB debugging on a security risk?", "Your TV only trusts the computer you allowed, but switch USB debugging off when you're done anyway. The new home screen keeps working without it."),
         ("Will Netflix, Prime Video and Hotstar still update?", "Yes. The Play Store is left alone, so your streaming apps keep updating as usual.")])

def block(slug, d):
    s = open(f'tools/{slug}/index.html', encoding='utf-8').read()
    key = re.search(r'Reel keyword: ([A-Z]+)', s)
    key = key.group(1).lower() if key else ''
    name = re.sub(r'<[^>]+>', '', re.search(r'<h1>(.*?)</h1>', s).group(1))
    about = ''
    if d['about'] or d['can']:
        fig = ''
        if key and os.path.exists(f'img/covers/{key}.webp'):
            href = REELS.get(key, 'https://instagram.com/aixsam.dev')
            fig = (f'<figure class="reelfig"><a href="{href}" target="_blank" rel="noopener"><img src="/img/covers/{key}.webp" '
                   f'alt="{name} reel cover by aixsam.dev" width="540" height="960" loading="lazy"></a>'
                   f'<figcaption>{"Watch the reel" if key in REELS else "From the reel"} · keyword {key.upper()}</figcaption></figure>')
        paras = ''.join(f'<p>{p}</p>' for p in d['about'])
        can = ''
        if d['can']:
            can = f'<h3 class="sub">What {name} can do</h3><ul class="can">' + ''.join(f'<li><b>{t}</b> {x}</li>' for t, x in d['can']) + '</ul>'
        about = f'<!--x:about--><section class="about"><div class="aboutgrid"><div><h2>What is {name}?</h2>{paras}{can}</div>{fig}</div></section><!--/x:about-->'
    faq = ''
    if d['faq']:
        faq = ('<!--x:faq--><section class="faq2"><h2>Questions people ask</h2>' +
               ''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in d['faq']) + '</section><!--/x:faq-->')
    return s, about, faq


for slug, d in C.items():
    s, about, faq = block(slug, d)
    s = re.sub(r'<!--x:about-->.*?<!--/x:about-->', '', s, flags=re.S)
    s = re.sub(r'<!--x:faq-->.*?<!--/x:faq-->', '', s, flags=re.S)
    if about:
        i = s.index('</section>', s.index('<section class="hero">')) + len('</section>')
        s = s[:i] + about + s[i:]
    if faq:
        s = s.replace('<section class="dm">', faq + '<section class="dm">', 1)
    open(f'tools/{slug}/index.html', 'w', encoding='utf-8').write(s)
    assert s.count('<!--x:faq-->') == (1 if faq else 0) and s.count('<!--x:about-->') == (1 if about else 0), slug
missing = {f.split('/')[1] for f in glob.glob('tools/*/index.html')} - set(C)
print('extra: updated', len(C), 'guides', '| no content for: ' + ', '.join(sorted(missing)) if missing else '')
