# Mahmoud Abdelhamid — AI Engineer

**Live portfolio:** https://0xuser100.github.io/

[![Validate and deploy portfolio](https://github.com/0Xuser100/0Xuser100.github.io/actions/workflows/pages.yml/badge.svg)](https://github.com/0Xuser100/0Xuser100.github.io/actions/workflows/pages.yml)

A responsive, bilingual English/Arabic portfolio with individually designed dark/light themes, a kinetic AI network illustration, an interactive project explorer, project case studies, career experience, project filters, and a downloadable CV.

The theme preference is saved locally. Decorative animations run automatically and respect device reduced-motion settings. The project explorer supports mouse, touch, and arrow-key navigation. Its architecture previews illustrate each project's workflow; they are not live product outputs.

The chat is a browser-local CV guide with prepared answers. It does not call an LLM or require API keys. Google Fonts is used for typography, with local system font fallbacks.

## Update the portfolio

Edit the website files in `dist/`, commit, and push to `main`. GitHub Actions validates the site and publishes the exact checked files to GitHub Pages automatically.

| File | Purpose |
| --- | --- |
| `dist/index.html` | Sections, contact links, and English/Arabic page copy |
| `dist/app.js` | Projects, case studies, filtering, translations, and CV guide answers |
| `dist/style.css` | Base theme and layout |
| `dist/refinements.css` | Portfolio presentation and responsive styling |
| `dist/motion.css` | Dark/light palettes, animated network, project explorer, and motion accessibility |
| `dist/motion.js` | Automatic animations, reveal effects, and reading progress |
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
node --check dist/motion.js
python scripts/check-site.py
```

## Deployment pipeline

```text
Push to main → syntax / asset / link checks → Pages artifact → deploy → verify live file hashes
Pull request → checks only
```

Track deployment under [Actions](https://github.com/0Xuser100/0Xuser100.github.io/actions). Manual deployment is available through **Actions → Validate and deploy portfolio → Run workflow**.

Repository **Settings → Pages → Source** must stay set to **GitHub Actions**. The workflow uses GitHub's built-in token and OIDC; no personal access token or custom deployment secret is needed.

The GitHub repository is the source for this deployment. Changes made only to the original Sites-hosted copy are separate and must also be committed here to appear on GitHub Pages.

GitHub Pages is the primary hosting for this portfolio. The post-deployment check compares the live homepage, JavaScript, styles, favicon, and CV with the repository. It catches a README/Jekyll page replacing the portfolio even when a deployment reports success.

---

## التعديل والنشر

عدّل الملفات داخل `dist/` ثم ارفع التعديل إلى فرع `main`. سيعمل GitHub Actions تلقائيًا لفحص الملفات ثم نشر الموقع. يمكنك متابعة النتيجة من تبويب **Actions**.

تعديلات نسخة Sites لا تنتقل وحدها إلى GitHub؛ يجب حفظها ورفعها إلى هذا المستودع أيضًا. الشات الحالي دليل للسيرة الذاتية بإجابات معدّة، ويعمل داخل المتصفح دون API أو مفاتيح سرية.
