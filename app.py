from pathlib import Path
import base64
import html

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# Henrique Duarte — Personal CV / R&D Website
# Rendering approach: the page is rendered inside a Streamlit
# HTML component so the HTML is interpreted correctly and never
# appears as raw text on the page.
# ============================================================

st.set_page_config(
    page_title="Henrique Duarte | Data Science & Process Intelligence",
    page_icon="HD",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit default padding/chrome around the custom page
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        #MainMenu, footer { visibility: hidden; }
        iframe { display:block; }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"


def asset_data_uri(filename: str, mime_type: str) -> str:
    """Convert a local asset to a browser-safe data URI."""
    path = ASSETS / filename
    if not path.exists():
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


hero_img = asset_data_uri("01.png", "image/png")
process_img = asset_data_uri("boardingsimulator.png", "image/png")
data_lab_img = asset_data_uri("1777885534233.png", "image/png")
profile_img = asset_data_uri("02.jpg", "image/jpeg")
cv_pdf = asset_data_uri("Henrique_Duarte_CV.pdf", "application/pdf")
dtu_img = asset_data_uri("dtu.png", "image/png")
isec_img = asset_data_uri("isec.png", "image/png")


# Public content. Edit here.
NAME = "Henrique Duarte"
EMAIL = "henriqduarte@outlook.pt"
CALENDLY = "https://calendly.com/henriqduarte/30min"
LINKEDIN = "https://www.linkedin.com/in/henriqduarte/"
BOARDING_OPTIMIZER_URL = "https://app.boarding-sequence-optimizer.henriqueduarte.com/"
MCDONALDS_ARTICLE_URL = "https://www.linkedin.com/pulse/fastest-restaurant-world-has-tomato-problem-henrique-duarte-hqzze/"

PAGE = f"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{html.escape(NAME)}</title>
<style>
    :root {{
        --ink: #111111;
        --muted: #5d5d5d;
        --muted2: #bab9b8;
        --line: #e6e2dc;
        --paper: #f6f3ee;
        --paper-2: #ffffff;
        --dark: #070708;
        --blue: #1700a6;
        --lime: #d7ff46;
        --soft-lime: #efffc1;
        --radius: 28px;
    }}

    * {{ box-sizing: border-box; }}

    html {{ scroll-behavior: smooth; }}

    body {{
        margin: 0;
        background: var(--paper);
        color: var(--ink);
        font-family: Inter, Arial, Helvetica, sans-serif;
        -webkit-font-smoothing: antialiased;
    }}

    a {{ color: inherit; }}

    .topbar {{
        height: 96px;
        background: #fff;
        border-top: 4px solid #222;
        border-bottom: 1px solid #ececec;
        display: grid;
        grid-template-columns: 330px 1fr 190px;
        align-items: center;
        padding: 0 32px;
        position: sticky;
        top: 0;
        z-index: 50;
    }}

    .brand {{
        display: flex;
        align-items: center;
        gap: 16px;
        font-weight: 900;
        letter-spacing: .12em;
        text-transform: uppercase;
        font-size: 18px;
        white-space: nowrap;
    }}

    .brand-mark {{
        width: 36px;
        height: 36px;
        background: #000;
        color: #fff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-style: italic;
        transform: skew(-8deg);
    }}

    .menu {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 34px;
    }}

    .menu-item {{
        position: relative;
        padding: 38px 0;
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .06em;
        text-decoration: underline;
        text-underline-offset: 3px;
        cursor: pointer;
        white-space: nowrap;
    }}

    .menu-item > a {{ text-decoration: none; }}

    .menu-item:hover .dropdown {{ display: block; }}

    .dropdown {{
        display: none;
        position: absolute;
        top: 82px;
        left: -22px;
        width: 250px;
        background: #fff;
        border: 1px solid #e2e2e2;
        box-shadow: 0 22px 60px rgba(0,0,0,.14);
        padding: 12px;
    }}

    .dropdown a {{
        display: block;
        padding: 13px 12px;
        text-transform: none;
        letter-spacing: 0;
        text-decoration: none;
        font-size: 14px;
        font-weight: 700;
        color: #111;
        border-radius: 10px;
    }}

    .dropdown a:hover {{ background: #f3f3f3; }}

    .cta-wrap {{ display: flex; justify-content: flex-end; }}

    .cta {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        min-width: 142px;
        padding: 17px 22px;
        background: var(--blue);
        color: #fff;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 900;
        font-size: 13px;
        text-transform: uppercase;
    }}

    .cta:hover {{ background: #0f0078; }}

    .section {{
        padding: 96px 48px;
        border-top: 1px solid var(--line);
    }}

    .section-inner {{
        max-width: 1220px;
        margin: 0 auto;
    }}

    .hero {{
        background: var(--paper);
        padding: 78px 48px 46px;
    }}

    .hero-grid {{
        max-width: 1220px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: minmax(0, 1.05fr) minmax(360px, .75fr);
        gap: 44px;
        align-items: stretch;
    }}

    .eyebrow {{
        color: var(--muted);
        font-size: 13px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: .16em;
        margin-bottom: 18px;
    }}

    h1, h2, h3, p {{ margin-top: 0; }}

    h1 {{
        font-size: clamp(64px, 7.7vw, 128px);
        line-height: .9;
        letter-spacing: -.075em;
        margin-bottom: 28px;
    }}

    h2 {{
        font-size: clamp(42px, 5vw, 76px);
        line-height: .96;
        letter-spacing: -.06em;
        margin-bottom: 28px;
    }}

    h3 {{
        font-size: 28px;
        line-height: 1.05;
        letter-spacing: -.035em;
        margin-bottom: 14px;
    }}

    .lead {{
        font-size: clamp(20px, 2.2vw, 30px);
        line-height: 1.28;
        max-width: 820px;
        margin-bottom: 30px;
    }}

    .body {{
        color: var(--muted);
        font-size: 18px;
        line-height: 1.7;
    }}

    .hero-actions {{ display: flex; gap: 14px; flex-wrap: wrap; }}

    .button {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 15px 18px;
        border-radius: 999px;
        border: 1px solid #111;
        font-weight: 900;
        text-decoration: none;
        background: #fff;
        color: #111;
    }}

    .button.primary {{ background: #111; color: #fff; }}
    .button.lime {{ background: var(--lime); color: #111; }}

    .hero-card {{
        background: #111;
        color: #fff;
        border-radius: var(--radius);
        overflow: hidden;
        min-height: 560px;
        display: grid;
        grid-template-rows: 1fr auto;
        box-shadow: 0 28px 70px rgba(0,0,0,.14);
    }}

    .hero-card img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

    .hero-card-footer {{
        padding: 26px;
        background: #111;
    }}

    .logo-strip {{
        max-width: 1220px;
        margin: 50px auto 0;
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }}

    .logo-chip {{
        border: 1px solid #111;
        padding: 12px 16px;
        border-radius: 999px;
        background: #fff;
        font-size: 14px;
        font-weight: 800;
    }}

    .two-col {{
        display: grid;
        grid-template-columns: .75fr 1.25fr;
        gap: 60px;
        align-items: start;
    }}

    .grid-3 {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
    }}

    .grid-2 {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 18px;
    }}

    .card {{
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 22px;
        padding: 26px;
        min-height: 220px;
        box-shadow: 0 14px 36px rgba(20,20,20,.04);
    }}

    .card.dark {{
        background: #111;
        color: #fff;
        border-color: #111;
    }}

    .card.lime {{
        background: var(--lime);
        border-color: #111;
    }}

    .meta {{
        color: var(--muted2);
        font-size: 12px;
        font-weight: 900;
        letter-spacing: .12em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }}

    .card.dark .meta {{ color: #fffafa; }}
    .card.lime .meta {{ color: #222; }}

    .number {{
        font-size: 54px;
        font-weight: 900;
        letter-spacing: -.075em;
        margin-bottom: 18px;
    }}

    .timeline {{ display: grid; gap: 16px; }}

    .timeline-item {{
        display: grid;
        grid-template-columns: 180px 1fr;
        gap: 24px;
        padding: 24px;
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 22px;
    }}

    .timeline-date {{
        font-size: 13px;
        font-weight: 900;
        color: var(--blue);
        text-transform: uppercase;
        letter-spacing: .08em;
    }}

    .tags {{ display: flex; gap: 10px; flex-wrap: wrap; margin-top: 20px; }}

    .tag {{
        display: inline-flex;
        padding: 9px 12px;
        border-radius: 999px;
        background: #fff;
        border: 1px solid var(--line);
        font-size: 14px;
        font-weight: 800;
    }}

    .image-block {{
        width: 100%;
        border-radius: 24px;
        border: 1px solid var(--line);
        display: block;
        overflow: hidden;
    }}

    .image-block img {{ width: 100%; display: block; }}

    .footer {{
        background: #111;
        color: #fff;
        padding: 90px 48px 40px;
    }}

    .footer-inner {{ max-width: 1220px; margin: 0 auto; }}

    .footer h2 {{ color: #fff; }}
    .footer .body {{ color: #d4d4d4; }}

    .footer-line {{
        margin-top: 70px;
        padding-top: 24px;
        border-top: 1px solid rgba(255,255,255,.16);
        display: flex;
        justify-content: space-between;
        color: #aaa;
        font-size: 14px;
    }}


    .article-list {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 22px;
        align-items: stretch;
    }}

    .article-card {{
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 26px;
        overflow: hidden;
        min-height: 100%;
        box-shadow: 0 14px 36px rgba(20,20,20,.05);
        display: flex;
        flex-direction: column;
        transition: transform .25s ease, box-shadow .25s ease;
    }}

    .article-card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 24px 70px rgba(20,20,20,.10);
    }}

    .article-image {{
        width: 100%;
        height: 230px;
        object-fit: cover;
        display: block;
        background: var(--paper-2);
    }}

    .article-card > .article-image {{
        height: auto;
        aspect-ratio: 16 / 10;
    }}

    .article-content {{
        padding: 26px;
        display: flex;
        flex-direction: column;
        flex: 1;
    }}

    .article-meta {{
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        align-items: center;
        margin-bottom: 18px;
    }}

    .article-badge {{
        display: inline-flex;
        padding: 7px 11px;
        border-radius: 999px;
        background: var(--soft-lime);
        color: #111;
        font-size: 12px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: .08em;
    }}

    .article-topic {{
        color: var(--muted);
        font-size: 13px;
        font-weight: 800;
    }}

    .article-card h3 {{
        margin-bottom: 14px;
    }}

    .article-card .body {{
        margin-bottom: 24px;
    }}

    .article-link {{
        margin-top: auto;
        color: #111 !important;
        font-size: 15px;
        font-weight: 900;
        text-decoration: none;
    }}

    .article-link:hover {{
        text-decoration: underline;
    }}

    @media (max-width: 1050px) {{
        .topbar {{
            height: auto;
            grid-template-columns: 1fr;
            gap: 18px;
            padding: 22px;
            position: relative;
        }}
        .menu {{ justify-content: flex-start; flex-wrap: wrap; gap: 16px 24px; }}
        .menu-item {{ padding: 0; }}
        .dropdown {{ position: static; box-shadow: none; margin-top: 10px; }}
        .cta-wrap {{ justify-content: flex-start; }}
        .hero-grid, .two-col, .grid-2, .grid-3, .article-list {{ grid-template-columns: 1fr; }}
        .timeline-item {{ grid-template-columns: 1fr; }}
        .hero-card {{ min-height: auto; }}
        .section, .hero, .footer {{ padding-left: 22px; padding-right: 22px; }}
    }}
</style>
</head>
<body>

<header class="topbar">
    <a class="brand" href="#top" style="text-decoration:none;">
        <span class="brand-mark">HD</span>
        <span>{html.escape(NAME)}</span>
    </a>

    

    <div class="cta-wrap">
        <a class="cta" href="{html.escape(CALENDLY, quote=True)}" target="_blank" rel="noopener noreferrer">LET'S TALK →</a>
    </div>
</header>

<main id="top">
    <section class="hero">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">Hey! Hello!</div>
                <h2>Henrique Duarte</h2>
                <p class="lead">
                
                This is my space.

                </p>
                <p class="lead">
                    Here I share my professional experience, reflections and experiments from personal research projects.
                </p>

                <p class="lead">
                    Welcome in.
                </p>
                <div class="hero-actions">
                    <a class="button primary" href="mailto:{html.escape(EMAIL)}">Email</a>
                    <a class="button" href="{html.escape(LINKEDIN)}" target="_blank">LinkedIn ↗</a>
                    <a class="button lime" href="{cv_pdf}" download="Henrique_Duarte_CV.pdf">Download CV</a>
                </div>
            </div>
            <aside class="hero-card">
                <img src="{hero_img}" alt="Abstract data systems visual" />
                <div class="hero-card-footer">
                    <div class="eyebrow" style="color:#aaa; margin-bottom:10px;">Current role</div>
                    <h3>Head of R&D and Data Science</h3>
                    <p class="body" style="color:#bab9b8;">Process Intelligence · Data Science · Consulting</p>
                </div>
            </aside>
        </div>
        <div class="logo-strip" aria-label="Focus areas">
        <div class="logo-chip">Process Intelligence</div>
            <div class="logo-chip">Data Science</div>
            <div class="logo-chip">B2B</div>
            <div class="logo-chip">Research</div>
            <div class="logo-chip">Process Oriented Solutions</div>
            <div class="logo-chip">AI</div>
            <div class="logo-chip">Automation</div>
            <div class="logo-chip">Computer Vision</div>
            
        </div>
    </section>

    <section id="about" class="section">
        <div class="section-inner two-col">
            <div>
                <div class="eyebrow">001 · Who I am</div>
                <h2>Data Scientist.</h2>
                <h3>Husband. Cyclist. Guitarrist. Wine Lover. Vinyl Collector. Family Cook. Pet Walker.</h3>
            </div>
            <div>
                <p class="body">
                    I have 10+ years of consulting experience across multiple industries. My work bridges academia and industry through research focused on data science, with hands-on experience in multicultural teams and banking clients across Europe and Africa.
                </p>
                <p class="body">
                    My work bridges academia and industry through research focused on data science, with hands-on experience in multicultural teams and B2B clients across Europe and Africa.
                </p>
                <p class="body">
                    I focus on applying data-driven insights to support process improvement, systems integration, automation, and better operational decision-making.
                </p>
            </div>
        </div>
    </section>

    <section id="capabilities" class="section">
        <div class="section-inner">
            <div class="eyebrow">010 · Capabilities</div>
            <h2>From data to operational intelligence.</h2>
            <div class="grid-3">
                <article id="process-intelligence" class="card lime">
                    <div class="number">01</div>
                    <div class="meta">Process Intelligence</div>
                    <h3>Business X-Ray</h3>
                    <p class="body" style="color:#222;">Process Mining/ Task Mining analysis from business process data, identifying variants, bottlenecks and opportunities for improvement.</p>
                </article>
                <article id="data-science" class="card">
                    <div class="number">02</div>
                    <div class="meta" style="color:#5d5d5d;">Data Science</div>
                    <h3>Enrichment of faulty data</h3>
                    <p class="body">Data extraction, transformation and cleaning from unstructured datasets, with analytics and modelling to turn information into decisions.</p>
                </article>
                <article id="automation" class="card dark">
                    <div class="number">03</div>
                    <div class="meta">Solutions and R&D</div>
                    <h3>Creating data-driven solutions</h3>
                    <p class="body" style="color:#bab9b8;">Research and development of innovative solutions based on multiple systems integration, task mining and automation.</p>
                </article>
            </div>
        </div>
    </section>


    <section id="experience" class="section">
        <div class="section-inner">
            <div class="eyebrow">011 · Experience</div>
            <h2>Consulting in software and data.</h2>
            <div class="timeline">
                
                <div class="timeline-item">
                    <div class="timeline-date">Oct 2021 — Present</div>
                    <div>
                        <h3>Head of R&D and Data Science · Breakawai</h3>
                        <p class="body">Copenhagen, Denmark · Process mining, task mining, data extraction, unstructured data cleaning, systems integration, R&D solutions and Agile implementation.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Jan 2024 — Present</div>
                    <div>
                        <h3>Portugal Country Manager · Breakawai</h3>
                        <p class="body">Porto, Portugal · Managing the technology hub in Portugal</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Jan 2018 — Dec 2019</div>
                    <div>
                        <h3>Experienced Programmer · Deloitte Portugal</h3>
                        <p class="body">Luanda, Angola · Maintenance and evolutive software activities using AS/400, COBOL, CLP and RPG; banking data transformation, reconciliation assets, client network and Agile implementation.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Jun 2017 — Dec 2017</div>
                    <div>
                        <h3>Junior Programmer · Deloitte Portugal</h3>
                        <p class="body">Lisbon, Portugal · Development of new SEPA directive for banking clients using C# and PL/SQL; maintenance and evolutive software using SSIS, SSRS and PL/SQL.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Sep 2016 — May 2017</div>
                    <div>
                        <h3>Trainee · Deloitte Portugal</h3>
                        <p class="body">Lisbon, Portugal · Development of assets for core banking systems, web and mobile test automation, and worldwide banking client collaboration.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">Feb 2016 — Jul 2016</div>
                    <div>
                        <h3>Intern · Space Layer Technologies</h3>
                        <p class="body">Coimbra, Portugal · Android applications focused on Internet of Things using Java, PHP, Android Studio and FIWARE.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="skills" class="section">
        <div class="section-inner grid-2">
            <div>
                <div class="eyebrow">100 · Skills</div>
                <h2>Technical stack.</h2>
                <p class="body">The toolkit behind the work: data platforms, programming, analytics, process intelligence and automation.</p>
                <div class="tags">
                    <span class="tag">Python</span>
                    <span class="tag">SQL</span>
                    <span class="tag">Algorithms</span>
                    <span class="tag">Automated Solutions</span>
                    <span class="tag">Process Mining</span>
                    <span class="tag">Task Mining</span>
                    <span class="tag">Machine Learning</span>
                    <span class="tag">Data Visualization</span>
                    <span class="tag">...</span>
                </div>
            </div>
        </div>
    </section>

    <section id="education" class="section">
        <div class="section-inner">
            <div class="eyebrow">101 · Education & Certifications</div>
            <h2>Academic foundation.</h2>
            <div class="grid-2">
                <article class="card">
                    <div class="meta">Education</div>
                    <img 
                        class="article-image" 
                        src="{dtu_img}" 
                        alt="Boarding Sequence Optimizer research article"
                    />
                    
                    <h3>MSc · Computer Science and Engineering</h3>
                    <p class="body">DTU — Technical University of Denmark · Copenhagen</p>
                    <p class="body">Feb 2020 — Jan 2022</p>
                </article>
                <article class="card">
                    <div class="meta">Education</div>
                    <img 
                        class="article-image" 
                        src="{isec_img}" 
                        alt="Boarding Sequence Optimizer research article"
                    />
                    <h3>Bachelor · Computer Science and Engineering</h3>
                    <p class="body">ISEC — Coimbra Superior Institute of Engineering · Coimbra</p>
                    <p class="body">Sep 2012 — Nov 2016</p>
                </article>
                <article class="card">
                    <div class="meta">Certifications</div>
                    <h3>Task Mining, Process Mining and IT Service Management</h3>
                    <p class="body">KYP.ai Task Mining Fundamentals · Apromore Process Mining Analysis Training Pathway · ITIL Foundation · Finastra Fusion Banking Essence.</p>
                </article>
                <article class="card">
                    <div class="meta">Languages</div>
                    <h3>Portuguese, English</h3>
                    <p class="body">Portuguese native, professional English background, and little Danish learning experience from work and study in Copenhagen.</p>
                </article>
            </div>
        </div>
    </section>

    <section id="research" class="section">
        <div class="section-inner">
            <div class="eyebrow">110 · R&D - Research & Development</div>

            <h2>Developments and research articles.</h2>

            <p class="body" style="max-width:820px; margin-bottom:36px;">
                A place where I publish technical experiments, research ideas, and practical notes around process intelligence,
                data science, automation, software development, optimization, and AI.
            </p>

            <div class="article-list">
                <article class="article-card">
                    <img 
                        class="article-image" 
                        src="{process_img}" 
                        alt="Boarding Sequence Optimizer research article"
                    />

                    <div class="article-content">
                        <div class="article-meta">
                            <span class="article-badge">Research Exercise</span>
                            <span class="article-topic">Aviation · Optimization · Simulator</span>
                        </div>

                        <h3>Optimization of aircraft boarding</h3>

                        <p class="body">
                            How simulation and process analysis can improve operational design and decision-making,
                            using the Boarding Sequence Optimizer as a practical research experiment.
                        </p>

                        <a 
                            class="article-link" 
                            href="{html.escape(BOARDING_OPTIMIZER_URL, quote=True)}" 
                            target="_blank" 
                            rel="noopener noreferrer"
                        >
                            Open simulator application →
                        </a>
                    </div>
                </article>

                <article class="article-card">
                    <img 
                        class="article-image" 
                        src="{data_lab_img}" 
                        alt="Data science article"
                    />

                    <div class="article-content">
                        <div class="article-meta">
                            <span class="article-badge">LinkedIn Article</span>
                            <span class="article-topic">Data Science · Optimization · Computer Vision</span>
                        </div>

                        <h3>The fastest restaurant in the world has a tomato problem</h3>

                        <p class="body">
                            An analysis of a McDonald's burger preparation process using computer vision. One finding stood out:
                            the tomato adds almost one extra second per burger, simply because of how it is stored.
                        </p>

                        <a 
                            class="article-link" 
                            href="{html.escape(MCDONALDS_ARTICLE_URL, quote=True)}" 
                            target="_blank" 
                            rel="noopener noreferrer"
                        >
                            Open LinkedIn article →
                        </a>
                    </div>
                </article>
            </div>
        </div>
    </section>
</main>

<script>
(function () {{
  function pageHeight() {{
    return Math.ceil(Math.max(
      document.body.scrollHeight,
      document.body.offsetHeight,
      document.documentElement.clientHeight,
      document.documentElement.scrollHeight,
      document.documentElement.offsetHeight
    ));
  }}

  function fit() {{
    var h = pageHeight();

    // Streamlit component resize API.
    try {{
      window.parent.postMessage({{
        isStreamlitMessage: true,
        type: "streamlit:setFrameHeight",
        height: h
      }}, "*");
    }} catch (e) {{}}

    // Fallback for browsers where direct iframe access is available.
    try {{
      var frames = window.parent.document.querySelectorAll('iframe');
      for (var i = 0; i < frames.length; i++) {{
        if (frames[i].contentWindow === window) {{
          frames[i].style.height = h + 'px';
          frames[i].setAttribute('height', h);
          break;
        }}
      }}
    }} catch (e) {{}}
  }}

  window.addEventListener('load', fit);
  window.addEventListener('resize', fit);
  if ('ResizeObserver' in window) {{
    new ResizeObserver(fit).observe(document.body);
  }}
  setTimeout(fit, 50);
  setTimeout(fit, 250);
  setTimeout(fit, 750);
}})();
</script>

<footer id="contact" class="footer">
    <div class="footer-inner">
        <div class="eyebrow" style="color:#aaa;">111 · Contact</div>
        <p class="body">Open for discussions around process intelligence, data science, task mining, AI, automation, and R&D collaborations.</p>
        <div class="hero-actions">
            <a class="button lime" href="mailto:{html.escape(EMAIL)}">Email</a>
            <a class="button" href="{html.escape(LINKEDIN)}" target="_blank">LinkedIn ↗</a>
            <a class="button" href="{cv_pdf}" download="Henrique_Duarte_CV.pdf">Download CV</a>
        </div>
        <div class="footer-line">
            <span>© 2026 Henrique Duarte</span>
            
        </div>
    </div>
</footer>

</body>
</html>
"""

# Start small and let the page resize itself to the exact footer height.
components.html(PAGE, height=1, scrolling=False)
