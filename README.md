# Mahmoud Abdelhamid — AI Engineer

**Live portfolio:** https://0xuser100.github.io/

[![Validate and deploy portfolio](https://github.com/0Xuser100/0Xuser100.github.io/actions/workflows/pages.yml/badge.svg)](https://github.com/0Xuser100/0Xuser100.github.io/actions/workflows/pages.yml)

A responsive, bilingual English/Arabic portfolio with dark/light themes, project case studies, career experience, project filters, and a downloadable CV.

The chat is a browser-local CV guide with prepared answers. It does not call an LLM or require API keys. Google Fonts is used for typography, with local system font fallbacks.

## Update the portfolio

Edit the website files in `dist/`, commit, and push to `main`. GitHub Actions validates the site and publishes the exact checked files to GitHub Pages automatically.

| File | Purpose |
| --- | --- |
| `dist/index.html` | Sections, contact links, and English/Arabic page copy |
| `dist/app.js` | Projects, case studies, filtering, translations, and CV guide answers |
| `dist/style.css` | Base theme and layout |
| `dist/refinements.css` | Portfolio presentation and responsive styling |
| `dist/Mahmoud_Abdulhamid.pdf` | Downloadable CV |
| `.github/workflows/pages.yml` | Validation and automatic Pages deployment |
| `scripts/check-site.py` | Local asset, link, translation, and metadata checks |

## Preview locally

Requires Python 3.9+ and Node.js for the JavaScript check. No dependencies or build step are needed.

```sh
python -m http.server 4173 --directory dist
```

Open http://localhost:4173/. Before pushing:

```sh
node --check dist/app.js
python scripts/check-site.py
```

## Deployment pipeline

```text
Push to main → syntax / asset / link checks → Pages artifact → deploy
Pull request → checks only
```

Track deployment under [Actions](https://github.com/0Xuser100/0Xuser100.github.io/actions). Manual deployment is available through **Actions → Validate and deploy portfolio → Run workflow**.

Repository **Settings → Pages → Source** must stay set to **GitHub Actions**. The workflow uses GitHub's built-in token and OIDC; no personal access token or custom deployment secret is needed.

The GitHub repository is the source for this deployment. Changes made only to the original Sites-hosted copy are separate and must also be committed here to appear on GitHub Pages.

---

## التعديل والنشر

عدّل الملفات داخل `dist/` ثم ارفع التعديل إلى فرع `main`. سيعمل GitHub Actions تلقائيًا لفحص الملفات ثم نشر الموقع. يمكنك متابعة النتيجة من تبويب **Actions**.

تعديلات نسخة Sites لا تنتقل وحدها إلى GitHub؛ يجب حفظها ورفعها إلى هذا المستودع أيضًا. الشات الحالي دليل للسيرة الذاتية بإجابات معدّة، ويعمل داخل المتصفح دون API أو مفاتيح سرية.
