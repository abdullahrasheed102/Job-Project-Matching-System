import requests

developer_skills = {
    "frontend": [
        "HTML",
        "CSS",
        "JavaScript",
        "TypeScript",
        "React",
        "Vue.js",
        "Next.js",
        "Angular",
        "Tailwind CSS",
        "Bootstrap"
    ],
    "backend": [
        "Node.js",
        "Express.js",
        "Django",
        "Flask",
        "FastAPI",
        "Spring Boot",
        "Ruby on Rails",
        "Laravel",
        "Go",
        "ASP.NET"
    ],
    "uiux": [
        "Figma",
        "Adobe XD",
        "Sketch",
        "InVision",
        "Framer",
        "Zeplin"
    ],
    "database": [
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "SQLite",
        "Redis",
        "Firebase Realtime DB",
        "DynamoDB",
        "Cassandra"
    ],
    "ai_services": [
        "langchain",
        "CrewAI",
        "langgraph",
    ],
    "cloud": [
        "AWS",
        "Azure",
        "Google Cloud Platform",
        "Firebase",
        "Vercel",
        "Netlify",
        "Cloudflare",
        "Heroku",
        "DigitalOcean"
    ],
    "other": [
        "Git",
        "Docker",
        "Kubernetes",
        "CI/CD",
        "REST API",
        "GraphQL",
        "JWT",
        "OAuth2",
        "Webpack",
        "ESLint"
    ]
}

response = requests.post(
    "http://127.0.0.1:5000/run",
    json={
        "topic": """JD

About Us We’re an AI‑native startup turning real‑time commerce signals into smart shopper and merchant experiences. A handful of flagship merchants are already live; now we’re preparing a public Shopify app. The Opportunity Take our v1 front‑end and dashboards and transform them into a merchant‑facing, next‑gen e‑commerce management platform. You’ll design the UX, wire up live data, and integrate our in‑house AI services so merchants can monitor, analyse, and update their stores in real time. What You’ll Do Build the UI – React / TypeScript / JavaScript, embedded in Shopify, with impeccable UX and visual polish. Upgrade the merchant console – move from passive dashboards to an action‑oriented interface that surfaces AI recommendations and lets merchants apply changes instantly. Own buyer‑tracking events – define schemas, instrument clients, stream data for heatmaps and experimentation. Transform storefronts on the fly – insert, remove, or reformat content via Shopify APIs and our AI services. Integrate external data tools – Google Analytics 4, Klaviyo, Yotpo, Segment, Algolia, Recharge, Attentive, Mixpanel, etc.—feeding rich merchant signals into our AI agent. Scale the backend – WebSockets on Lambda and AWS Fargate, API Gateway, DynamoDB + Redis. Ship secure code – OAuth, JWT/Cognito, IAM, encryption at rest & in transit. Automate everything – Docker, GitHub Actions CI/CD, feature flags, safe rollbacks. Keep an eye on prod – logs, metrics, traces, and be ready to jump in when something breaks (no formal on‑call rota). Document & demo – share progress early, give and receive feedback openly. Must‑Haves - 5+ years building production web apps (2+ years lead). - React/TypeScript mastery and standout UX sensibility. - Deep Shopify experience (Hydrogen, Liquid, embedded apps, theme‑agnostic code). - Real‑time systems and WebSocket architectures. - Event‑driven tracking frameworks and data privacy know‑how. - AWS chops – Fargate, API Gateway, Lambda, DynamoDB, SQS, IaC. - Secure‑by‑design mindset; proven safe deployment strategies. - External data‑tool integrations (GA4, Klaviyo, Yotpo, Segment, Algolia, Recharge, Attentive, Mixpanel). - Docker+GitHub Actions workflow experience. - Clear communicator who thrives on constructive feedback. Nice‑To‑Haves - Redis or similar in‑memory stores. - Serverless front‑end hosting (Vercel, Cloudflare Pages). - Public Shopify app lifecycle experience (app review, billing APIs). - Familiarity with AI/LLM dev tools (Copilot, Cursor, Replit, etc.). How We Work Remote‑first, async‑friendly, and opinionated about quality. We move fast, measure, and iterate—while keeping healthy work hours. Application Process Ready to build the future of AI‑driven commerce? Apply with your GitHub, LinkedIn, and one example of a system you designed end‑to‑end.""",
        "developer_skills": developer_skills
    }
)
print(response.json())