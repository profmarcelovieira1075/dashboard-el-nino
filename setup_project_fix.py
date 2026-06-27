#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

print("=" * 60)
print("CRIANDO ARQUIVOS DO PROJETO")
print("=" * 60)

# 1. package.json
package = {
    "name": "dashboard-el-nino-2026-27",
    "version": "1.0.0",
    "description": "Dashboard El Nino 2026/2027",
    "scripts": {
        "dev": "vite",
        "build": "vite build",
        "deploy": "vercel --prod"
    },
    "dependencies": {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "@supabase/supabase-js": "^2.38.0"
    }
}
Path('package.json').write_text(json.dumps(package, indent=2), encoding='utf-8')
print("[OK] package.json")

# 2. .env.example
env_example = """VITE_SUPABASE_URL=https://seu-projeto.supabase.co
VITE_SUPABASE_ANON_KEY=sua-chave-api
VERCEL_TOKEN=seu-token-vercel
"""
Path('.env.example').write_text(env_example, encoding='utf-8')
print("[OK] .env.example")

# 3. .gitignore
gitignore = """.env.local
node_modules/
dist/
.vercel/
"""
Path('.gitignore').write_text(gitignore, encoding='utf-8')
print("[OK] .gitignore")

# 4. vercel.json
vercel = {
    "buildCommand": "npm run build",
    "outputDirectory": "dist"
}
Path('vercel.json').write_text(json.dumps(vercel, indent=2), encoding='utf-8')
print("[OK] vercel.json")

# 5. README.md
readme = """# Dashboard El Nino 2026/2027 - SEDEC-RJ

Supabase + Vercel + React

## Setup

npm install
npm run dev
"""
Path('README.md').write_text(readme, encoding='utf-8')
print("[OK] README.md")

# 6. Pastas
for folder in ['public', 'src/components', 'src/lib']:
    Path(folder).mkdir(parents=True, exist_ok=True)
print("[OK] Pastas criadas")

print("\n[SUCESSO!]")
print("Arquivos criados. Execute: npm install")
