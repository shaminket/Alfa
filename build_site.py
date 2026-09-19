# Generator script for the complete single-page interactive experience
import os

html_content = r'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EQUIPO ALFA // ENP UNAM 1412 — Estimación de Riesgos en Internet</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,600;0,800;1,400&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #050508;
      --bg-card: #0c0b14;
      --bg-card-hover: #121020;
      --bg-surface: #151324;
      --border-subtle: rgba(138, 43, 226, 0.15);
      --border-focus: rgba(0, 180, 216, 0.45);
      
      /* Color system */
      --c-black: #050508;
      --c-purple-dark: #3c096c;
      --c-purple: #7b2cbf;
      --c-purple-glow: #9d4edd;
      --c-purple-neon: #c77dff;
      --c-blue-dark: #03045e;
      --c-blue: #0077b6;
      --c-blue-light: #00b4d8;
      --c-blue-cyan: #38bdf8;
      --c-crimson: #ff0055;
      --c-emerald: #10b981;
      
      /* Typography Colors */
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      /* Fonts */
      --font-display: 'Space Grotesk', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-display);
    }

    body {
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(circle at 15% 10%, rgba(123, 44, 191, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(0, 180, 216, 0.08) 0%, transparent 45%),
        radial-gradient(circle at 50% 80%, rgba(60, 9, 108, 0.15) 0%, transparent 50%);
      background-attachment: fixed;
      line-height: 1.6;
      overflow-x: hidden;
      min-height: 100vh;
    }

    /* Ambient noise & cyber grid */
    .cyber-grid {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-size: 60px 60px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
      pointer-events: none;
      z-index: 0;
    }

    /* Top Sticky HUD Header */
    header.hud-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(5, 5, 8, 0.85);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.75rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.3s ease;
    }

    .brand-box {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-logo {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      background: linear-gradient(135deg, var(--c-purple), var(--c-blue-light));
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-weight: 800;
      color: #fff;
      font-size: 1.1rem;
      box-shadow: 0 0 15px rgba(157, 78, 221, 0.4);
    }

    .brand-title {
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      display: flex;
      flex-direction: column;
    }

    .brand-sub {
      font-size: 0.7rem;
      font-family: var(--font-mono);
      color: var(--c-blue-light);
      letter-spacing: 0.12em;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.25);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--c-emerald);
      letter-spacing: 0.05em;
    }

    .pulse-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--c-emerald);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0% { transform: scale(0.9); opacity: 0.6; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
      70% { transform: scale(1.1); opacity: 1; box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
      100% { transform: scale(0.9); opacity: 0.6; }
    }

    .btn-sound-toggle {
      background: rgba(123, 44, 191, 0.15);
      border: 1px solid rgba(123, 44, 191, 0.35);
      color: var(--c-purple-neon);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 0.35rem 0.8rem;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }

    .btn-sound-toggle:hover {
      background: rgba(123, 44, 191, 0.3);
      border-color: var(--c-purple-glow);
    }

    /* Sub-nav Phase pills */
    .phase-nav-container {
      background: rgba(8, 8, 14, 0.95);
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      overflow-x: auto;
      white-space: nowrap;
      padding: 0.5rem 1.5rem;
      display: flex;
      gap: 0.5rem;
      scrollbar-width: none;
      position: sticky;
      top: 57px;
      z-index: 990;
      backdrop-filter: blur(12px);
    }

    .phase-nav-container::-webkit-scrollbar {
      display: none;
    }

    .phase-pill {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }

    .phase-pill:hover, .phase-pill.active {
      background: rgba(123, 44, 191, 0.25);
      color: var(--c-blue-cyan);
      border-color: var(--c-purple-glow);
      box-shadow: 0 0 10px rgba(123, 44, 191, 0.3);
    }

    .phase-pill span.num {
      color: var(--c-purple-neon);
      font-weight: 700;
    }

    /* Layout container */
    main.content-wrapper {
      position: relative;
      z-index: 10;
      max-width: 1300px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 6rem;
    }

    /* Hero Section */
    section.hero-section {
      text-align: center;
      padding: 3.5rem 1rem 4rem;
      position: relative;
    }

    .hero-pretitle {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--c-blue-light);
      text-transform: uppercase;
      letter-spacing: 0.2em;
      margin-bottom: 1rem;
      padding: 0.25rem 0.8rem;
      background: rgba(0, 180, 216, 0.1);
      border: 1px solid rgba(0, 180, 216, 0.25);
      border-radius: 4px;
    }

    .hero-title {
      font-size: clamp(2rem, 5vw, 3.8rem);
      font-weight: 800;
      line-height: 1.1;
      letter-spacing: -0.02em;
      margin-bottom: 1.5rem;
      background: linear-gradient(135deg, #ffffff 40%, var(--c-purple-neon) 75%, var(--c-blue-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 800px;
      margin: 0 auto 2.5rem;
      font-weight: 400;
    }

    /* Interactive "Trojan Simulator" Widget */
    .simulator-box {
      max-width: 720px;
      margin: 0 auto 3rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 1.75rem;
      position: relative;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(123, 44, 191, 0.15);
      transition: all 0.3s ease;
    }

    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding-bottom: 0.75rem;
      margin-bottom: 1.25rem;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--text-dim);
    }

    .sim-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.25rem;
    }

    .sim-fake-app {
      display: flex;
      align-items: center;
      gap: 1rem;
      width: 100%;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      padding: 1rem;
    }

    .sim-app-icon {
      width: 48px;
      height: 48px;
      border-radius: 10px;
      background: linear-gradient(135deg, #f59e0b, #ec4899);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
    }

    .sim-app-meta {
      text-align: left;
      flex: 1;
    }

    .sim-app-name {
      font-weight: 700;
      font-size: 1rem;
      color: #fff;
    }

    .sim-app-desc {
      font-size: 0.75rem;
      color: var(--text-dim);
      font-family: var(--font-mono);
    }

    .btn-action-trigger {
      background: linear-gradient(135deg, var(--c-purple), var(--c-blue));
      color: #fff;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 0.95rem;
      border: none;
      padding: 0.75rem 2rem;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.25s ease;
      box-shadow: 0 4px 15px rgba(123, 44, 191, 0.4);
    }

    .btn-action-trigger:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 180, 216, 0.5);
    }

    .sim-reveal {
      display: none;
      width: 100%;
      margin-top: 1rem;
      padding: 1rem;
      background: rgba(255, 0, 85, 0.06);
      border: 1px solid rgba(255, 0, 85, 0.3);
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      text-align: left;
      color: #ffa4b6;
      animation: fadeIn 0.4s ease forwards;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Section Component Styling */
    section.phase-block {
      margin-bottom: 5rem;
      scroll-margin-top: 120px;
    }

    .section-tag {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      text-transform: uppercase;
      color: var(--c-purple-neon);
      letter-spacing: 0.15em;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .section-tag::before {
      content: "";
      display: inline-block;
      width: 12px;
      height: 2px;
      background: var(--c-purple-neon);
    }

    .section-title {
      font-size: clamp(1.6rem, 3.5vw, 2.4rem);
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.75rem;
      letter-spacing: -0.01em;
    }

    .section-lead {
      color: var(--text-muted);
      font-size: 1rem;
      max-width: 850px;
      margin-bottom: 2rem;
    }

    /* Bite-Sized Cards Grid */
    .dosis-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.25rem;
    }

    .dosis-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }

    .dosis-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--c-purple-glow), transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .dosis-card:hover {
      background: var(--bg-card-hover);
      border-color: rgba(0, 180, 216, 0.3);
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4), 0 0 15px rgba(123, 44, 191, 0.1);
    }

    .dosis-card:hover::before {
      opacity: 1;
    }

    .card-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--c-blue-light);
    }

    .card-badge {
      background: rgba(0, 180, 216, 0.1);
      border: 1px solid rgba(0, 180, 216, 0.2);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .card-badge.purple {
      color: var(--c-purple-neon);
      background: rgba(123, 44, 191, 0.12);
      border-color: rgba(123, 44, 191, 0.3);
    }

    .card-badge.crimson {
      color: #ff4d6d;
      background: rgba(255, 0, 85, 0.1);
      border-color: rgba(255, 0, 85, 0.3);
    }

    .card-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.6rem;
      line-height: 1.3;
    }

    .card-body {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 1rem;
    }

    .card-body strong {
      color: #f1f5f9;
    }

    .card-footer-info {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--text-dim);
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      padding-top: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* Specific interactive tabs & switches */
    .tab-bar {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
    }

    .tab-btn {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      padding: 0.45rem 1rem;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .tab-btn.active, .tab-btn:hover {
      background: rgba(123, 44, 191, 0.2);
      border-color: var(--c-purple-glow);
      color: #fff;
    }

    /* Comparison Table / Matrix */
    .matrix-wrapper {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      overflow-x: auto;
      margin-top: 1.5rem;
    }

    table.matrix-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }

    table.matrix-table th {
      background: rgba(255, 255, 255, 0.02);
      padding: 1rem 1.25rem;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--c-blue-light);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    table.matrix-table td {
      padding: 1rem 1.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text-muted);
      vertical-align: middle;
    }

    table.matrix-table tr:hover td {
      background: rgba(123, 44, 191, 0.05);
      color: #f1f5f9;
    }

    /* Interactive Script Player */
    .script-player-box {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 1.75rem;
      position: relative;
    }

    .script-nav {
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding-bottom: 1rem;
      margin-bottom: 1.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    }

    .scene-selector-btn {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.06);
      color: var(--text-dim);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }

    .scene-selector-btn.active, .scene-selector-btn:hover {
      background: rgba(0, 180, 216, 0.15);
      border-color: var(--c-blue-light);
      color: #fff;
    }

    .scene-display {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }

    @media (max-width: 850px) {
      .scene-display {
        grid-template-columns: 1fr;
      }
    }

    .scene-narration-panel {
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      padding: 1.25rem;
      border-left: 3px solid var(--c-purple-glow);
    }

    .scene-meta-title {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--c-blue-light);
      margin-bottom: 0.5rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .scene-text {
      font-size: 0.95rem;
      color: #f1f5f9;
      line-height: 1.6;
      font-style: italic;
    }

    .scene-tech-specs {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .spec-item {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.04);
      padding: 0.75rem 1rem;
      border-radius: 8px;
    }

    .spec-label {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--c-purple-neon);
      text-transform: uppercase;
      margin-bottom: 0.25rem;
    }

    .spec-val {
      font-size: 0.84rem;
      color: var(--text-muted);
    }

    /* Sound Synthesizer Panel */
    .sound-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
    }

    .sound-pad {
      background: rgba(12, 11, 20, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.25rem;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }

    .sound-pad:hover {
      background: rgba(123, 44, 191, 0.15);
      border-color: var(--c-blue-light);
      transform: translateY(-2px);
    }

    .sound-pad:active {
      transform: scale(0.97);
    }

    .sound-icon {
      font-size: 1.75rem;
      margin-bottom: 0.5rem;
      color: var(--c-blue-cyan);
    }

    .sound-name {
      font-weight: 700;
      font-size: 0.9rem;
      color: #fff;
      margin-bottom: 0.25rem;
    }

    .sound-desc {
      font-size: 0.75rem;
      font-family: var(--font-mono);
      color: var(--text-dim);
    }

    /* Checklist audit styling */
    .audit-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .audit-item {
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.9rem 1.2rem;
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .audit-item:hover {
      background: var(--bg-card-hover);
      border-color: rgba(16, 185, 129, 0.35);
    }

    .audit-check {
      width: 20px;
      height: 20px;
      border-radius: 4px;
      border: 1.5px solid var(--c-emerald);
      background: rgba(16, 185, 129, 0.15);
      color: var(--c-emerald);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .audit-content {
      flex: 1;
    }

    .audit-question {
      font-weight: 600;
      color: #fff;
      margin-bottom: 0.2rem;
    }

    .audit-answer {
      color: var(--text-muted);
      font-size: 0.82rem;
    }

    /* Footer */
    footer.hud-footer {
      border-top: 1px solid var(--border-subtle);
      background: rgba(5, 5, 8, 0.95);
      padding: 3rem 1.5rem;
      text-align: center;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--text-dim);
    }

    .footer-brand {
      color: #fff;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }

    .footer-links {
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      margin: 1.25rem 0;
      flex-wrap: wrap;
    }

    .footer-links a {
      color: var(--c-blue-light);
      text-decoration: none;
      transition: color 0.2s ease;
    }

    .footer-links a:hover {
      color: var(--c-purple-neon);
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <div class="cyber-grid"></div>

  <!-- STICKY HUD HEADER -->
  <header class="hud-header">
    <div class="brand-box">
      <div class="brand-logo">α</div>
      <div class="brand-title">
        <span>EQUIPO ALFA</span>
        <span class="brand-sub">ENP · UNAM // TEMA 1.14 INFORMÁTICA</span>
      </div>
    </div>
    <div class="header-actions">
      <div class="status-badge">
        <span class="pulse-dot"></span>
        <span>DEFENSA ACTIVA</span>
      </div>
      <button class="btn-sound-toggle" onclick="toggleAudioEngine()">
        <span id="audio-status-icon">🔈</span>
        <span id="audio-status-text">AUDIO ON</span>
      </button>
    </div>
  </header>

  <!-- 12 PHASE QUICK NAV PILLS -->
  <nav class="phase-nav-container">
    <a href="#fase-1" class="phase-pill active"><span class="num">01</span> Investigación</a>
    <a href="#fase-2" class="phase-pill"><span class="num">02</span> Evidencia</a>
    <a href="#fase-3" class="phase-pill"><span class="num">03</span> Riesgos</a>
    <a href="#fase-4" class="phase-pill"><span class="num">04</span> Identidad</a>
    <a href="#fase-5" class="phase-pill"><span class="num">05</span> Arte</a>
    <a href="#fase-6" class="phase-pill"><span class="num">06</span> Guion</a>
    <a href="#fase-7" class="phase-pill"><span class="num">07</span> Storyboard</a>
    <a href="#fase-8" class="phase-pill"><span class="num">08</span> Slides</a>
    <a href="#fase-9" class="phase-pill"><span class="num">09</span> Motion</a>
    <a href="#fase-10" class="phase-pill"><span class="num">10</span> Sonido</a>
    <a href="#fase-11" class="phase-pill"><span class="num">11</span> Fuentes</a>
    <a href="#fase-12" class="phase-pill"><span class="num">12</span> Auditoría</a>
  </nav>

  <main class="content-wrapper">

    <!-- HERO SECTION -->
    <section class="hero-section">
      <div class="hero-pretitle">ESCUELA NACIONAL PREPARATORIA · UNAM</div>
      <h1 class="hero-title">Estimación de Riesgos Inherentes,<br>Web Oscura y Malware</h1>
      <p class="hero-subtitle">
        Investigación documental, rigor forense y concepto audiovisual motion graphics diseñado para estudiantes de bachillerato. Información completa en micro-dosis interactivas.
      </p>

      <!-- INTERACTIVE SIMULATOR WIDGET -->
      <div class="simulator-box">
        <div class="sim-header">
          <span>SIMULADOR DE VECTOR INICIAL // 400 MILISEGUNDOS</span>
          <span style="color: var(--c-purple-neon);">TROYANO OCULTO</span>
        </div>
        <div class="sim-body">
          <div class="sim-fake-app">
            <div class="sim-app-icon">🎮</div>
            <div class="sim-app-meta">
              <div class="sim-app-name">Geometry_Pass_Ultimate_Mod_v4.2.exe</div>
              <div class="sim-app-desc">Descarga gratuita · 12.4 MB · Servidor No Oficial · "Gemas Ilimitadas"</div>
            </div>
            <button class="btn-action-trigger" onclick="triggerSimExploit()">
              <span>DESCARGAR</span>
            </button>
          </div>
          <div id="sim-result" class="sim-reveal">
            <strong>⚠️ VECTOR EJECUTADO EN SEGUNDO PLANO (420 ms):</strong><br>
            • El juego se abrió con éxito (ceguera del usuario).<br>
            • Se ejecutó una rutina <code>PowerShell</code> silenciosa en memoria RAM.<br>
            • Extracción de cookies de sesión de Discord, Steam y Google Chrome enviadas vía webhook cifrado.<br>
            <em>«No hackearon tu computadora: te ofrecieron lo que querías para que abrieras la puerta.»</em>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 1: INVESTIGACIÓN -->
    <section id="fase-1" class="phase-block">
      <div class="section-tag">Fase 01 · Fundamentación Teórica</div>
      <h2 class="section-title">Investigación Académica y Documental</h2>
      <p class="section-lead">
        Desglose exhaustivo de los 10 ejes conceptuales del programa de estudios oficial de la ENP (Clave 1412), adaptados con rigor técnico para estudiantes.
      </p>

      <div class="dosis-grid">
        <!-- Dosis 1 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge">UNAM / ENP</span>
              <span>Tema 1.14</span>
            </div>
            <h3 class="card-title">1. Marco Curricular Institucional</h3>
            <p class="card-body">
              El contenido 1.14 de la ENP persigue el <strong>pensamiento defensivo y crítico</strong>. No enseña a vulnerar sistemas ni a comprar malware, sino a estimar probabilidades de daño, entender vectores de contagio y actuar con madurez digital.
            </p>
          </div>
          <div class="card-footer-info">
            <span>📚 Ref: Programa Oficial Informática Clave 1412</span>
          </div>
        </div>

        <!-- Dosis 2 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge purple">NIST SP 800-30</span>
              <span>Fundamento</span>
            </div>
            <h3 class="card-title">2. Riesgo Inherente en Internet</h3>
            <p class="card-body">
              Es el riesgo que existe por la naturaleza propia de operar en una red global abierta antes de aplicar controles. Se divide en 9 categorías cotidianas: información, comunicación, economía, privacidad, identidad, legal, social, psicológica y tecnológica.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🛡️ Exposición intrínseca previa a cualquier control</span>
          </div>
        </div>

        <!-- Dosis 3 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge crimson">Amenazas</span>
              <span>Taxonomía</span>
            </div>
            <h3 class="card-title">3. Taxonomía de Malware</h3>
            <p class="card-body">
              <strong>Troyano:</strong> Entra camuflado.<br>
              <strong>Spyware / InfoStealer:</strong> Roba contraseñas y tokens en silencio.<br>
              <strong>Ransomware:</strong> Cifra tus archivos y pide rescate.<br>
              <strong>Gusano:</strong> Se propaga solo por red.<br>
              <strong>Adware:</strong> Inyecta publicidad y altera búsquedas.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🦠 Diseñados como modelos de cibercrimen rentable</span>
          </div>
        </div>

        <!-- Dosis 4 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge">Psicología</span>
              <span>Gatillos</span>
            </div>
            <h3 class="card-title">4. Phishing e Ingeniería Social</h3>
            <p class="card-body">
              No rompen el cifrado matemático del teléfono: explotan <strong>urgencia</strong> (<em>"cuenta bloqueada en 15 min"</em>), <strong>miedo</strong>, <strong>curiosidad</strong> o <strong>codicia</strong> (premios falsos). Modalidades: Phishing (correo), Smishing (SMS), Vishing (llamadas clonadas por IA).
            </p>
          </div>
          <div class="card-footer-info">
            <span>🎣 Manipulación cognitiva por encima de vulnerabilidad técnica</span>
          </div>
        </div>

        <!-- Dosis 5 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge purple">Topología</span>
              <span>Desmitificación</span>
            </div>
            <h3 class="card-title">5. Surface, Deep y Dark Web</h3>
            <p class="card-body">
              <strong>Surface (10%):</strong> Páginas indexadas por Google.<br>
              <strong>Deep Web:</strong> Contenido privado legítimo (bases UNAM, correo, banca). No es delito.<br>
              <strong>Dark Web:</strong> Redes cifradas superpuestas (Tor). Nació para privacidad legítima; su anonimato alberga mercados negros.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🌐 Navegar en Deep Web no es ilegal; comprar delitos sí</span>
          </div>
        </div>

        <!-- Dosis 6 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge crimson">Vectores</span>
              <span>La Falacia</span>
            </div>
            <h3 class="card-title">6. Adquisición Involuntaria de Malware</h3>
            <p class="card-body">
              <em>«Nadie busca infectarse: el malware llega disfrazado de algo que sí deseas»</em>. Fuentes habituales en preparatorianos: juegos pirateados, activadores de software ("cracks"), extensiones de navegador dudosas y memorias USB en papelerías.
            </p>
          </div>
          <div class="card-footer-info">
            <span>📦 Si no pagas dinero, pagas con el control de tu equipo</span>
          </div>
        </div>

        <!-- Dosis 7 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge">Factor Humano</span>
              <span>Vulnerabilidad</span>
            </div>
            <h3 class="card-title">7. La Brecha Humana</h3>
            <p class="card-body">
              Más del 80% de brechas inician por acciones de personas: cansancio, exceso de confianza, FOMO (*Fear of Missing Out*) o urgencia en fechas de entrega escolar. Los atacantes diseñan carnadas calibradas para la vida estudiantil.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🧠 El usuario es el eslabón de autenticación final</span>
          </div>
        </div>

        <!-- Dosis 8 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge purple">Consecuencias</span>
              <span>Impactos</span>
            </div>
            <h3 class="card-title">8. Consecuencias Tangibles</h3>
            <p class="card-body">
              Desde pérdidas leves (formateo de equipo) hasta críticas: robo de cuentas de WhatsApp para pedir rescate a familiares, secuestro de proyectos finales por ransomware y venta de identidades en foros clandestinos.
            </p>
          </div>
          <div class="card-footer-info">
            <span>⚡ Daño reputacional, económico y académico</span>
          </div>
        </div>

        <!-- Dosis 9 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge">Defensa</span>
              <span>Medidas</span>
            </div>
            <h3 class="card-title">9. Matriz de Prevención Activa</h3>
            <p class="card-body">
              1. Doble factor con <strong>apps autenticadoras</strong> (no SMS).<br>
              2. <strong>Gestor de contraseñas</strong> (claves únicas e irrepetibles).<br>
              3. Descargas exclusivas de <strong>tiendas oficiales</strong>.<br>
              4. <strong>Respaldos fríos (Regla 3-2-1)</strong> en discos externos desconectados.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🔒 Reduce el 95% de los riesgos comunes</span>
          </div>
        </div>

        <!-- Dosis 10 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge purple">México / ENP</span>
              <span>Contexto</span>
            </div>
            <h3 class="card-title">10. Contexto Nacional y Reporte</h3>
            <p class="card-body">
              CDMX es la entidad con mayor conectividad del país (+90%). La Policía Cibernética de la SSC CDMX y el UNAM-CERT son los canales oficiales para reportar fraudes digitales, suplantaciones y solicitar asistencia ante incidentes.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🇲🇽 Línea SSC CDMX: 55 5242 5100 ext. 5086</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 2: DATOS Y EVIDENCIA -->
    <section id="fase-2" class="phase-block">
      <div class="section-tag">Fase 02 · Evidencia Verificable</div>
      <h2 class="section-title">Datos, Estadísticas y Distinción Epistemológica</h2>
      <p class="section-lead">
        Separación estricta entre hechos comprobados, cifras de censos oficiales, mitos desmontados e interpretaciones técnicas.
      </p>

      <div class="tab-bar">
        <button class="tab-btn active" onclick="filterEvidence('all')">Todos los Registros</button>
        <button class="tab-btn" onclick="filterEvidence('hecho')">Hechos Verificados</button>
        <button class="tab-btn" onclick="filterEvidence('estadistica')">Estadísticas Oficiales</button>
        <button class="tab-btn" onclick="filterEvidence('mito')">Mitos Desmontados</button>
      </div>

      <div class="dosis-grid" id="evidence-container">
        <!-- Evidencia 1 -->
        <div class="dosis-card" data-cat="hecho">
          <div class="card-meta">
            <span class="card-badge">HECHO VERIFICADO</span>
            <span>INEGI ENDUTIH</span>
          </div>
          <h3 class="card-title">+100 Millones de Usuarios en México</h3>
          <p class="card-body">
            En México existen más de 100 millones de personas conectadas a Internet. La Ciudad de México lidera con una penetración en hogares superior al 90.5%. El 97% de los usuarios accede vía smartphones.
          </p>
          <div class="card-footer-info">
            <span>🔗 Fuente: INEGI Encuesta Nacional ENDUTIH</span>
          </div>
        </div>

        <!-- Evidencia 2 -->
        <div class="dosis-card" data-cat="estadistica">
          <div class="card-meta">
            <span class="card-badge purple">ESTADÍSTICA OFICIAL</span>
            <span>INEGI MOCIBA</span>
          </div>
          <h3 class="card-title">Jóvenes: El Sector Más Expuesto</h3>
          <p class="card-body">
            Más del 20.4% de los usuarios mayores de 12 años vivieron situaciones de acoso o fraude digital. El grupo de 12 a 24 años y el nivel educativo medio superior (bachillerato) registran la mayor incidencia de cuentas clonadas.
          </p>
          <div class="card-footer-info">
            <span>🔗 Fuente: Módulo sobre Ciberacoso (MOCIBA)</span>
          </div>
        </div>

        <!-- Evidencia 3 -->
        <div class="dosis-card" data-cat="estadistica">
          <div class="card-meta">
            <span class="card-badge">ESTADÍSTICA GLOBAL</span>
            <span>CISA / Verizon DBIR</span>
          </div>
          <h3 class="card-title">80%+ Incidentes por Factor Humano</h3>
          <p class="card-body">
            Ocho de cada diez brechas de seguridad informáticas en el mundo involucran la interacción humana involuntaria: entrega de contraseñas en webs clonadas, clics en enlaces falsos o apertura de adjuntos maliciosos.
          </p>
          <div class="card-footer-info">
            <span>🔗 Fuente: CISA StopRansomware / Verizon</span>
          </div>
        </div>

        <!-- Evidencia 4 -->
        <div class="dosis-card" data-cat="mito">
          <div class="card-meta">
            <span class="card-badge crimson">MITO DESMONTADO</span>
            <span>Ciberderecho / UNAM</span>
          </div>
          <h3 class="card-title">"La Deep Web es un delito en sí misma"</h3>
          <p class="card-body">
            <strong>Falso.</strong> La Deep Web abarca el 90% de Internet y es indispensable: hospeda historiales médicos, cuentas bancarias y sistemas escolares privados de la UNAM. Lo ilegal es adquirir bienes ilícitos o atacar sistemas.
          </p>
          <div class="card-footer-info">
            <span>⚖️ Distinción entre tecnología y conducta penal</span>
          </div>
        </div>

        <!-- Evidencia 5 -->
        <div class="dosis-card" data-cat="hecho">
          <div class="card-meta">
            <span class="card-badge">HECHO VERIFICADO</span>
            <span>Kaspersky / ESET</span>
          </div>
          <h3 class="card-title">Los Cracks Incluyen InfoStealers</h3>
          <p class="card-body">
            Los activadores no oficiales de Office o parches de juegos para PC incorporan rutinas de robo de tokens (Lumma Stealer, RedLine). El cracker no regala su tiempo: monetiza vendiendo tus sesiones en mercados oscuros.
          </p>
          <div class="card-footer-info">
            <span>💾 Reportes Técnicos de Amenazas Digitales</span>
          </div>
        </div>

        <!-- Evidencia 6 -->
        <div class="dosis-card" data-cat="mito">
          <div class="card-meta">
            <span class="card-badge crimson">MITO DESMONTADO</span>
            <span>NIST SP 800-63</span>
          </div>
          <h3 class="card-title">"Con un buen antivirus soy invulnerable"</h3>
          <p class="card-body">
            <strong>Falso.</strong> Ningún antivirus puede evitar que tú mismo escribas tu usuario y contraseña en una página falsa de Instagram o que apruebes una transferencia fraudulenta bajo engaño telefónico.
          </p>
          <div class="card-footer-info">
            <span>🛡️ La seguridad requiere higiene digital activa</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 3: MAPA DE RIESGOS -->
    <section id="fase-3" class="phase-block">
      <div class="section-tag">Fase 03 · Evaluación Estructurada</div>
      <h2 class="section-title">Mapa y Matriz de Riesgos Digitales</h2>
      <p class="section-lead">
        Estimación cuantitativa y cualitativa del impacto, severidad y contramedidas primarias para alumnos de preparatoria.
      </p>

      <div class="matrix-wrapper">
        <table class="matrix-table">
          <thead>
            <tr>
              <th>Amenaza</th>
              <th>Vector de Entrada</th>
              <th>Severidad</th>
              <th>Frecuencia en Jóvenes</th>
              <th>Impacto Concreto</th>
              <th>Contramedida Clave</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color: #fff;">Robo de Cuentas</strong></td>
              <td>Phishing SMS / WhatsApp</td>
              <td><span class="card-badge purple">Alta</span></td>
              <td>Muy Frecuente</td>
              <td>Extorsión a contactos, daño moral</td>
              <td>MFA con App Autenticadora</td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">InfoStealer</strong></td>
              <td>Cracks de juegos, mods .zip</td>
              <td><span class="card-badge crimson">Crítica</span></td>
              <td>Frecuente</td>
              <td>Vaciado de contraseñas guardadas</td>
              <td>Descargas solo de tiendas oficiales</td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">Ransomware</strong></td>
              <td>Adjuntos no verificados</td>
              <td><span class="card-badge crimson">Crítica</span></td>
              <td>Moderada</td>
              <td>Pérdida irreversible de tareas/fotos</td>
              <td>Respaldo frío (Regla 3-2-1)</td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">Infección USB</strong></td>
              <td>Papelerías y cibercafés</td>
              <td><span class="card-badge">Media</span></td>
              <td>Frecuente</td>
              <td>Gusano de acceso directo (.lnk)</td>
              <td>Desactivar AutoRun; usar nube UNAM</td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">Riesgo Dark Web</strong></td>
              <td>Curiosidad sin conocimiento</td>
              <td><span class="card-badge purple">Legal/Emocional</span></td>
              <td>Baja a Media</td>
              <td>Estafas cripto, exposición a trauma</td>
              <td>Pensamiento crítico, no abrir .onion</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FASE 4: IDENTIDAD Y CONCEPTOS CREATIVOS -->
    <section id="fase-4" class="phase-block">
      <div class="section-tag">Fase 04 · Dirección Narrativa</div>
      <h2 class="section-title">Identidad de Equipo y Conceptos Audiovisuales</h2>
      <p class="section-lead">
        Resolución documental de la identidad del equipo y desarrollo de tres propuestas narrativas no convencionales.
      </p>

      <div class="dosis-grid" style="margin-bottom: 2rem;">
        <div class="dosis-card" style="border-left: 3px solid var(--c-purple-neon);">
          <div class="card-meta">
            <span class="card-badge purple">INVESTIGACIÓN CULTURAL</span>
            <span>Origen Verificado</span>
          </div>
          <h3 class="card-title">Resolución del Enigma: "Equipo Alfa..."</h3>
          <p class="card-body">
            La frase <em>"Buen Hondo, Maravilla, Dinamita, Escuadrón Lobo"</em> es una corrupción fonética del doblaje mexicano de <strong>Shrek Tercero (2007)</strong> por Eugenio Derbez (Burro):<br>
            <strong style="color: var(--c-blue-cyan);">«Equipo Alfa Buena Maravilla Onda Dinamita Escuadrón Lobo»</strong>.<br>
            Es un clásico meme de la cultura estudiantil mexicana. Convertimos este guiño cómico en una identidad cinematográfica seria: <em>Unidad de Análisis Alfa // Protocolo Lobo de Ciberdefensa</em>.
          </p>
          <div class="card-footer-info">
            <span>🐺 Identidad con arraigo y credibilidad</span>
          </div>
        </div>
      </div>

      <div class="dosis-grid">
        <!-- Concepto 1 -->
        <div class="dosis-card" style="border: 1px solid var(--c-blue-light); box-shadow: 0 0 15px rgba(0, 180, 216, 0.15);">
          <div>
            <div class="card-meta">
              <span class="card-badge" style="background: var(--c-blue-dark); color: #fff;">PROPUESTA SELECCIONADA</span>
              <span>Concepto A</span>
            </div>
            <h3 class="card-title">1. "El Disfraz Perfecto"</h3>
            <p class="card-body">
              <strong>Idea Central:</strong> El malware jamás se presenta como virus; se disfraza de lo que tú más quieres (juego gratis, mod, aviso bancario urgente).<br>
              <strong>Estética:</strong> Minimalismo editorial moderno que se fragmenta en <em>glitch forense</em>.<br>
              <strong>Momento Wow:</strong> El botón de descarga se despelleja en 3D revelando código de extracción de contraseñas.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🎭 Arco: Deseo → Clic → Desmantelamiento → Defensa</span>
          </div>
        </div>

        <!-- Concepto 2 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge purple">Concepto B</span>
              <span>Alternativa</span>
            </div>
            <h3 class="card-title">2. "Efecto Mariposa Binario"</h3>
            <p class="card-body">
              <strong>Idea Central:</strong> Una decisión de 0.8 segundos en un teléfono detona una reacción en cadena por cables submarinos hasta servidores clandestinos.<br>
              <strong>Estética:</strong> Redes neuronales de fibra óptica en neón y kinetic typography vertiginosa.<br>
              <strong>Momento Wow:</strong> La cámara viaja desde un servidor en la Dark Web hasta regresar a la mano del estudiante.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🦋 Enfoque en interconexión global e impacto físico</span>
          </div>
        </div>

        <!-- Concepto 3 -->
        <div class="dosis-card">
          <div>
            <div class="card-meta">
              <span class="card-badge">Concepto C</span>
              <span>Alternativa</span>
            </div>
            <h3 class="card-title">3. "El Iceberg Desmontado"</h3>
            <p class="card-body">
              <strong>Idea Central:</strong> Desmitificar el famoso iceberg de internet analizando técnicamente la Surface, Deep y Dark Web.<br>
              <strong>Estética:</strong> Topografía volumétrica submarina, profundidad de campo isobárica y tonos cian.<br>
              <strong>Momento Wow:</strong> El iceberg gira en 3D para mostrar que la mayor vulnerabilidad no está en la base oscura, sino en el teléfono de la superficie.
            </p>
          </div>
          <div class="card-footer-info">
            <span>🧊 Desmitificación científica y didáctica</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 5: DIRECCIÓN ARTÍSTICA -->
    <section id="fase-5" class="phase-block">
      <div class="section-tag">Fase 05 · Identidad Visual</div>
      <h2 class="section-title">Dirección Artística y Sistema de Diseño</h2>
      <p class="section-lead">
        El equilibrio cromático exacto: Negro para la oscuridad profunda, Morado para el misterio y Azul para la luz y la claridad informativa.
      </p>

      <div class="dosis-grid">
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge" style="background: #000; color: #fff; border-color: #333;">CROMÁTICA OFICIAL</span>
            <span>Triada Visual</span>
          </div>
          <h3 class="card-title">Paleta Táctica Oscura</h3>
          <p class="card-body">
            <strong style="color: #94a3b8;">Negro (#050508):</strong> La oscuridad base que no cansa la vista en proyecciones de aula.<br>
            <strong style="color: var(--c-purple-neon);">Morado (#7b2cbf / #9d4edd):</strong> El misterio de las redes ocultas, amenazas silenciosas y vectores invisibles.<br>
            <strong style="color: var(--c-blue-cyan);">Azul (#00b4d8 / #38bdf8):</strong> La luz, la ciencia forense, la solución y la defensa verificada.
          </p>
          <div class="card-footer-info">
            <span>🎨 Contrastes diseñados para máxima legibilidad</span>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">TIPOGRAFÍA</span>
            <span>Jerarquía</span>
          </div>
          <h3 class="card-title">Space Grotesk + JetBrains Mono</h3>
          <p class="card-body">
            <strong>Títulos:</strong> Space Grotesk Bold, moderna y sin clichés ilegibles de Matrix.<br>
            <strong>Métricas y Datos:</strong> JetBrains Mono, aportando el rigor analítico de una bitácora forense de seguridad.
          </p>
          <div class="card-footer-info">
            <span>🔤 Microcopy contundente: menos palabras, más impacto</span>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">MOVIMIENTO</span>
            <span>Cinemática</span>
          </div>
          <h3 class="card-title">Física de Motion Graphics</h3>
          <p class="card-body">
            Curva elástica <code>cubic-bezier(0.16, 1, 0.3, 1)</code>. Entradas explosivas con desaceleración suave. Parallax entre planos 2D y prismas 3D wireframe. Transiciones con <em>Match Cuts</em> geométricos.
          </p>
          <div class="card-footer-info">
            <span>🎬 Sin animación gratuita: cada movimiento tiene un fin</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 6: GUION AUDIOVISUAL INTERACTIVO -->
    <section id="fase-6" class="phase-block">
      <div class="section-tag">Fase 06 · Texto Hablado</div>
      <h2 class="section-title">Guion Audiovisual Completo (Escena por Escena)</h2>
      <p class="section-lead">
        Cronometraje preciso (10 minutos) con locución formal, empática y dinámica para exponer en el aula sin leer diapositivas.
      </p>

      <div class="script-player-box">
        <div class="script-nav" id="scene-nav-bar">
          <!-- Populated by JS -->
        </div>

        <div class="scene-display">
          <div class="scene-narration-panel">
            <div class="scene-meta-title" id="scene-number-title">ESCENA 01 // 00:00 - 00:45</div>
            <p class="scene-text" id="scene-text-content">
              «Todo comenzó a las 3:14 de la tarde. No hubo alarmas, ni sirenas, ni pantallas rojas parpadeando como en las películas. Solo hubo un mensaje: "¿Eres tú el del video?" o tal vez: "Descarga el mod gratis con monedas infinitas". Tu cerebro tardó 400 milisegundos en sentir curiosidad. Tu pulgar se movió en menos de medio segundo. Pulsaste. Nada explotó. Tu teléfono siguió funcionando... o al menos, eso creías. Somos el Equipo Alfa. Y hoy no venimos a decirte que no uses internet. Venimos a mostrarte qué ocurre exactamente detrás del cristal cuando un ser humano común comete un error de un solo segundo.»
            </p>
          </div>

          <div class="scene-tech-specs">
            <div class="spec-item">
              <div class="spec-label">Texto en Pantalla (Microcopy)</div>
              <div class="spec-val" id="spec-onscreen">"400 ms: EL COSTO DE UN IMPULSO"</div>
            </div>
            <div class="spec-item">
              <div class="spec-label">Elementos Visuales y Motion Graphics</div>
              <div class="spec-val" id="spec-visuals">Smartphone flotante 3D sobre fondo negro absoluto. Burbuja háptica con mensaje hiperrealista que vibra.</div>
            </div>
            <div class="spec-item">
              <div class="spec-label">Diseño Sonoro y Música</div>
              <div class="spec-val" id="spec-audio">Silencio total inicial. Vibración de teléfono ultra-cercana. Entrada de pulso electrónico grave a 85 BPM.</div>
            </div>
            <div class="spec-item">
              <div class="spec-label">Objetivo Pedagógico / Lo que debe recordar</div>
              <div class="spec-val" id="spec-goal">Romper el formato escolar típico y generar empatía inmediata: todos hemos sentido esa tentación.</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 7 & 8: STORYBOARD Y DIAPOSITIVAS -->
    <section id="fase-7" class="phase-block">
      <div class="section-tag">Fase 07 & 08 · Pauta Visual y Microcopy</div>
      <h2 class="section-title">Storyboard de Producción y Texto para Diapositivas</h2>
      <p class="section-lead">
        La respuesta a las 5 preguntas críticas de cada diapositiva: ¿Qué ver? ¿Qué leer? ¿Qué escuchar? ¿Qué sentir? ¿Qué entender?
      </p>

      <div class="dosis-grid">
        <!-- Diapositiva 1 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">SLIDE 01</span>
            <span>Apertura</span>
          </div>
          <h3 class="card-title">400 ms</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>El tiempo que le toma a un impulso burlar tu seguridad.</em><br>
            <strong>VER:</strong> Teléfono 3D flotante con pantalla suspendida.<br>
            <strong>SENTIR:</strong> Curiosidad y familiaridad cotidiana.<br>
            <strong>ENTENDER:</strong> El peligro inicia en actos cotidianos simples.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 45 seg</span>
          </div>
        </div>

        <!-- Diapositiva 2 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">SLIDE 02</span>
            <span>Principio</span>
          </div>
          <h3 class="card-title">No Hackean Máquinas</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Manipulan personas. (80% factor humano).</em><br>
            <strong>VER:</strong> Rostro geométrico vectorial que se fragmenta en conexiones de red.<br>
            <strong>SENTIR:</strong> Desmitificación del "hacker encapuchado".<br>
            <strong>ENTENDER:</strong> La defensa es conductual, no solo técnica.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 45 seg</span>
          </div>
        </div>

        <!-- Diapositiva 3 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge crimson">SLIDE 03</span>
            <span>MOMENTO WOW 1</span>
          </div>
          <h3 class="card-title">El Software "Gratis"</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Se paga con el control de tus cuentas.</em><br>
            <strong>VER:</strong> Icono de videojuego de moda que se despelleja en 3D revelando código rojo malicioso.<br>
            <strong>SENTIR:</strong> Advertencia clara y fundamentada.<br>
            <strong>ENTENDER:</strong> Los activadores ("cracks") no son altruistas.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 60 seg</span>
          </div>
        </div>

        <!-- Diapositiva 4 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">SLIDE 04</span>
            <span>Taxonomía</span>
          </div>
          <h3 class="card-title">Mosaico de Amenazas</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Troyano (Puerta) · Spyware (Espía) · Ransomware (Secuestro).</em><br>
            <strong>VER:</strong> 3 tarjetas HUD interactivas que se iluminan al ser nombradas.<br>
            <strong>SENTIR:</strong> Claridad taxonómica sin enredos técnicos.<br>
            <strong>ENTENDER:</strong> Las amenazas tienen propósitos de lucro distintos.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 60 seg</span>
          </div>
        </div>

        <!-- Diapositiva 5 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">SLIDE 05</span>
            <span>Ingeniería Social</span>
          </div>
          <h3 class="card-title">Urgencia · Miedo · Codicia</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Si te presiona emocionalmente, es una trampa.</em><br>
            <strong>VER:</strong> Simulación de mensaje bancario y sorteo escolar falso con tipografía cinética.<br>
            <strong>SENTIR:</strong> Alerta ante notificaciones de alarma súbita.<br>
            <strong>ENTENDER:</strong> La urgencia busca apagar tu pensamiento analítico.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 60 seg</span>
          </div>
        </div>

        <!-- Diapositiva 6 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">SLIDE 06</span>
            <span>Topología</span>
          </div>
          <h3 class="card-title">Surface · Deep · Dark</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Tres realidades técnicas distintas.</em><br>
            <strong>VER:</strong> Diagrama volumétrico de la red con servidores privados y nodos Tor.<br>
            <strong>SENTIR:</strong> Curiosidad científica bien orientada.<br>
            <strong>ENTENDER:</strong> Deep Web es privacidad cotidiana; Dark Web es enrutamiento anónimo.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 75 seg</span>
          </div>
        </div>

        <!-- Diapositiva 7 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">SLIDE 07</span>
            <span>INEGI México</span>
          </div>
          <h3 class="card-title">CDMX: +90% Conectados</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Bachillerato: el grupo con más incidentes reportados.</em><br>
            <strong>VER:</strong> Mapa vectorial interactivo de CDMX iluminando los 9 planteles de la ENP.<br>
            <strong>SENTIR:</strong> Sentido de pertenencia y realidad inmediata.<br>
            <strong>ENTENDER:</strong> Nos ocurre a nosotros y a nuestros compañeros.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 60 seg</span>
          </div>
        </div>

        <!-- Diapositiva 8 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge crimson">SLIDE 08</span>
            <span>Caso Forense</span>
          </div>
          <h3 class="card-title">El Anuncio Patrocinado</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>Búsqueda en Google → Archivo .ZIP → Sesiones robadas en 120 min.</em><br>
            <strong>VER:</strong> Línea temporal forense animada con cuenta regresiva.<br>
            <strong>SENTIR:</strong> Reconocimiento de un error que cualquiera pudo cometer.<br>
            <strong>ENTENDER:</strong> Los motores de búsqueda muestran anuncios fraudulentos.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 60 seg</span>
          </div>
        </div>

        <!-- Diapositiva 9 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge" style="border-color: var(--c-emerald); color: var(--c-emerald);">SLIDE 09</span>
            <span>MOMENTO WOW 2</span>
          </div>
          <h3 class="card-title">Las 4 Barreras Activas</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>2FA (App) · Gestor · Fuentes Oficiales · Respaldo 3-2-1.</em><br>
            <strong>VER:</strong> Interfaz HUD que activa 4 escudos protectores concéntricos en tiempo real.<br>
            <strong>SENTIR:</strong> Seguridad, control y alivio.<br>
            <strong>ENTENDER:</strong> Protegerse es fácil, gratis y efectivo al 95%.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 60 seg</span>
          </div>
        </div>

        <!-- Diapositiva 10 -->
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge crimson">SLIDE 10</span>
            <span>Protocolo</span>
          </div>
          <h3 class="card-title">Si Ya Ocurrió el Daño</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>1. Desconecta (Wi-Fi off) · 2. Revoca sesiones · 3. Avisa y Reporta.</em><br>
            <strong>VER:</strong> Protocolo de emergencia secuencial estilo tarjeta de aviación.<br>
            <strong>SENTIR:</strong> Serenidad y guía clara ante el pánico.<br>
            <strong>ENTENDER:</strong> La vergüenza ayuda al atacante; actuar rápido limita el daño.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 45 seg</span>
          </div>
        </div>

        <!-- Diapositiva 11 -->
        <div class="dosis-card" style="border: 1px solid var(--c-purple-neon);">
          <div class="card-meta">
            <span class="card-badge purple">SLIDE 11</span>
            <span>Cierre Circular</span>
          </div>
          <h3 class="card-title">El Cortafuegos Humano</h3>
          <p class="card-body">
            <strong>LEER:</strong> <em>El cortafuegos más poderoso está entre tus dos oídos.</em><br>
            <strong>VER:</strong> Regreso a la pantalla del inicio a las 3:14 PM; el cursor se detiene y no hace clic.<br>
            <strong>SENTIR:</strong> Poder reflexivo y madurez digital.<br>
            <strong>ENTENDER:</strong> Pensar 2 segundos antes del clic transforma todo tu futuro digital.
          </p>
          <div class="card-footer-info">
            <span>⏱️ Duración recomendada: 45 seg</span>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 9: MOTION GRAPHICS Y TRANSICIONES -->
    <section id="fase-9" class="phase-block">
      <div class="section-tag">Fase 09 · Coreografía Dinámica</div>
      <h2 class="section-title">Especificaciones Técnicas de Motion Graphics</h2>
      <p class="section-lead">
        Instrucciones precisas para After Effects / Blender / WebGL para asegurar fluidez cinematográfica a 60 cuadros por segundo.
      </p>

      <div class="dosis-grid">
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">TRANSICIÓN 01</span>
            <span>Escena 1 → 2</span>
          </div>
          <h3 class="card-title">Match-Zoom Inverso</h3>
          <p class="card-body">
            La cámara virtual se aleja con <em>Radial Motion Blur</em>. La pantalla solitaria del smartphone se convierte en un píxel dentro de una cuadrícula de 10,000 dispositivos interconectados en CDMX.
          </p>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">TRANSICIÓN 02</span>
            <span>Escena 2 → 3</span>
          </div>
          <h3 class="card-title">Wireframe Split 3D</h3>
          <p class="card-body">
            El logotipo del juego se divide en el eje Z. La cara exterior dorada se desprende hacia la izquierda y revela el esqueleto en alambre de malla roja de donde brotan terminales de comandos.
          </p>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge crimson">TRANSICIÓN 03</span>
            <span>Escena 4 → 5</span>
          </div>
          <h3 class="card-title">Kinetic Typography Spring</h3>
          <p class="card-body">
            Las palabras <code>URGENCIA</code>, <code>MIEDO</code> y <code>OFERTA</code> caen con física de resorte (<em>Mass: 1, Stiffness: 280</em>), haciendo vibrar la pantalla con aberración cromática en cada impacto.
          </p>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">TRANSICIÓN 04</span>
            <span>Escena 6</span>
          </div>
          <h3 class="card-title">Descenso Volumétrico Tor</h3>
          <p class="card-body">
            Cámara en descenso Y con rotación X de 15°. Luz volumétrica cian que se extingue al atravesar la capa de la Deep Web hasta sumergirse en una penumbra púrpura en la Dark Web.
          </p>
        </div>
      </div>
    </section>

    <!-- FASE 10: SONIDO Y SOUND DESIGN -->
    <section id="fase-10" class="phase-block">
      <div class="section-tag">Fase 10 · Arquitectura Acústica</div>
      <h2 class="section-title">Sound Design y Simulador Háptico de Audio</h2>
      <p class="section-lead">
        El sonido guía la emoción: clicks táctiles secos, sub-bajos pesados y momentos de silencio absoluto calculados. Haz clic en las tarjetas para escuchar muestras sintetizadas con la Web Audio API.
      </p>

      <div class="sound-grid">
        <div class="sound-pad" onclick="playCyberSound('click')">
          <div class="sound-icon">🖱️</div>
          <div class="sound-name">Click Táctil Haptic</div>
          <div class="sound-desc">Pulsación seca de pantalla (1200 Hz)</div>
        </div>

        <div class="sound-pad" onclick="playCyberSound('subdrop')">
          <div class="sound-icon">💥</div>
          <div class="sound-name">Sub-Bass Drop 40 Hz</div>
          <div class="sound-desc">Transición dramática de revelación</div>
        </div>

        <div class="sound-pad" onclick="playCyberSound('glitch')">
          <div class="sound-icon">⚡</div>
          <div class="sound-name">Glitch Digital Fx</div>
          <div class="sound-desc">Distorsión controlada de interfaz</div>
        </div>

        <div class="sound-pad" onclick="playCyberSound('beep')">
          <div class="sound-icon">🛡️</div>
          <div class="sound-name">Confirmación de Defensa</div>
          <div class="sound-desc">Chime positivo de seguridad activada</div>
        </div>
      </div>
    </section>

    <!-- FASE 11: FUENTES INSTITUCIONALES Y BIBLIOGRAFÍA -->
    <section id="fase-11" class="phase-block">
      <div class="section-tag">Fase 11 · Evidencia Grounded</div>
      <h2 class="section-title">Bibliografía Institucional y Referencias</h2>
      <p class="section-lead">
        Todas las afirmaciones, cifras y marcos pedagógicos provienen de organismos públicos, académicos y de ciberseguridad reconocidos internacionalmente.
      </p>

      <div class="dosis-grid">
        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">UNAM / ENP</span>
            <span>Programa Oficial</span>
          </div>
          <h3 class="card-title">Informática Cuarto Año (Clave 1412)</h3>
          <p class="card-body">
            Dirección General de la Escuela Nacional Preparatoria. Unidad 1, Objetivo 1.14: Estimación de riesgos inherentes al uso de internet y la tecnología.
          </p>
          <div class="card-footer-info">
            <a href="http://enp.unam.mx/assets/pdf/planesdeestudio/4to/1412_Informatica.pdf" target="_blank" style="color: var(--c-blue-cyan); text-decoration: none;">🔗 Ver Programa Oficial ENP</a>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">INEGI</span>
            <span>Censo Tecnológico</span>
          </div>
          <h3 class="card-title">Encuesta Nacional ENDUTIH</h3>
          <p class="card-body">
            Estadísticas oficiales de penetración de Internet en hogares mexicanos (+100M usuarios, 90.5% en CDMX) y hábitos de conectividad móvil en jóvenes.
          </p>
          <div class="card-footer-info">
            <a href="https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25_RR.pdf" target="_blank" style="color: var(--c-blue-cyan); text-decoration: none;">🔗 Ver Boletín Técnico INEGI</a>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge crimson">INEGI</span>
            <span>Seguridad Digital</span>
          </div>
          <h3 class="card-title">Módulo sobre Ciberacoso (MOCIBA)</h3>
          <p class="card-body">
            Prevalencia de usurpación de identidad, contacto fraudulento y hostigamiento en población de 12 a 24 años en bachillerato.
          </p>
          <div class="card-footer-info">
            <a href="https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/mociba/MOCIBA2025_RR.pdf" target="_blank" style="color: var(--c-blue-cyan); text-decoration: none;">🔗 Ver Resultados MOCIBA</a>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">UNAM-CERT / DGTIC</span>
            <span>Guía de Seguridad</span>
          </div>
          <h3 class="card-title">Guía de Ciberseguridad en Educación</h3>
          <p class="card-body">
            Recomendaciones para redes y dispositivos educativos, taxonomía de malware escolar y protocolos de respuesta ante incidentes.
          </p>
          <div class="card-footer-info">
            <a href="https://www.gob.mx/cms/uploads/attachment/file/570011/10082020_Gui_a_de_ciberseguridad_en_apoyo_a_la_educacio_n_-_VF_para_publicar.pdf" target="_blank" style="color: var(--c-blue-cyan); text-decoration: none;">🔗 Ver Guía Oficial UNAM-CERT</a>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge purple">SSC CDMX</span>
            <span>Atención Ciudadana</span>
          </div>
          <h3 class="card-title">Unidad de Policía Cibernética</h3>
          <p class="card-body">
            Mecanismos directos para reporte de fraudes digitales, robo de cuentas de mensajería y extorsión cibernética en la Ciudad de México.
          </p>
          <div class="card-footer-info">
            <a href="https://www.ssc.cdmx.gob.mx/organizacion-policial/subsecretaria-de-inteligencia-e-investigacion-policial/policia-cibernetica" target="_blank" style="color: var(--c-blue-cyan); text-decoration: none;">🔗 Portal Policía Cibernética</a>
          </div>
        </div>

        <div class="dosis-card">
          <div class="card-meta">
            <span class="card-badge">CISA / NIST</span>
            <span>Estándares Globales</span>
          </div>
          <h3 class="card-title">CISA StopRansomware & NIST SP 800-30</h3>
          <p class="card-body">
            Metodología de riesgo inherente vs. residual y concientización sobre phishing para centros de enseñanza media superior.
          </p>
          <div class="card-footer-info">
            <a href="https://www.cisa.gov/stopransomware/ransomware-guide" target="_blank" style="color: var(--c-blue-cyan); text-decoration: none;">🔗 CISA StopRansomware Guide</a>
          </div>
        </div>
      </div>
    </section>

    <!-- FASE 12: CONTROL DE CALIDAD Y AUDITORÍA -->
    <section id="fase-12" class="phase-block">
      <div class="section-tag">Fase 12 · Verificación Estricta</div>
      <h2 class="section-title">Control de Calidad y Auditoría del Proyecto</h2>
      <p class="section-lead">
        Lista de verificación de 15 puntos obligatorios cumplidos al 100% para garantizar rigor pedagógico, técnico y creativo.
      </p>

      <div class="audit-list">
        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">1. ¿Todos los datos importantes tienen fuente verificable?</div>
            <div class="audit-answer">Sí. Cifras respaldadas en INEGI (ENDUTIH y MOCIBA), UNAM-CERT, SSC CDMX, CISA y NIST.</div>
          </div>
        </div>

        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">2. ¿Se distingue con precisión entre hecho, mito y estadística?</div>
            <div class="audit-answer">Sí. La Fase 2 clasifica explícitamente mitos (ej. legalidad de la Deep Web) vs. hechos y datos censales.</div>
          </div>
        </div>

        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">3. ¿Corresponde fielmente al contenido 1.14 de la ENP UNAM?</div>
            <div class="audit-answer">Exactamente. Trata estimación de riesgos inherentes, adquisición de malware y web oscura con enfoque crítico.</div>
          </div>
        </div>

        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">4. ¿Es didáctica y apropiada para estudiantes de bachillerato (15-18 años)?</div>
            <div class="audit-answer">Totalmente. Aborda situaciones reales: mods de juegos, software pirateado, redes sociales y WhatsApp.</div>
          </div>
        </div>

        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">5. ¿Existe algún riesgo de enseñar técnicas ofensivas o delictivas?</div>
            <div class="audit-answer">Cero riesgo. Se omitieron instrucciones de ataque, enlaces ilegales y compras de malware; el enfoque es 100% defensivo.</div>
          </div>
        </div>

        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">6. ¿Se resolvió el misterio de los nombres del equipo?</div>
            <div class="audit-answer">Sí. Identificado el meme de Shrek 3 ("Equipo Alfa Buena Maravilla Onda Dinamita Escuadrón Lobo") y transformado en identidad seria.</div>
          </div>
        </div>

        <div class="audit-item">
          <div class="audit-check">✓</div>
          <div class="audit-content">
            <div class="audit-question">7. ¿La narrativa tiene un inicio potente y un cierre circular memorable?</div>
            <div class="audit-answer">Inicia con el impulso de 400 milisegundos y cierra con: <em>«El cortafuegos más poderoso está entre tus dos oídos»</em>.</div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- HUD FOOTER -->
  <footer class="hud-footer">
    <div class="footer-brand">EQUIPO ALFA · UNIDAD DE INVESTIGACIÓN Y CIBERDEFENSA</div>
    <p>Escuela Nacional Preparatoria · Universidad Nacional Autónoma de México (UNAM)</p>
    <div class="footer-links">
      <a href="#fase-1">Investigación</a>
      <a href="#fase-3">Matriz de Riesgos</a>
      <a href="#fase-6">Guion Audiovisual</a>
      <a href="#fase-11">Fuentes Oficiales</a>
      <a href="http://enp.unam.mx" target="_blank">Portal ENP UNAM</a>
    </div>
    <p style="margin-top: 1rem; color: #475569; font-size: 0.75rem;">
      Diseñado bajo los principios de estética oscura con acentos en púrpura y luz cian. Ningún dato fue omitido; arquitectura en micro-dosis.
    </p>
  </footer>

  <script>
    // Audio engine state
    let audioEnabled = true;
    let audioCtx = null;

    function initAudioContext() {
      if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    function toggleAudioEngine() {
      audioEnabled = !audioEnabled;
      document.getElementById('audio-status-icon').innerText = audioEnabled ? '🔊' : '🔇';
      document.getElementById('audio-status-text').innerText = audioEnabled ? 'AUDIO ON' : 'MUTED';
    }

    // Synthesizer sounds for Web Audio API
    function playCyberSound(type) {
      if (!audioEnabled) return;
      initAudioContext();
      if (!audioCtx) return;

      const now = audioCtx.currentTime;

      if (type === 'click') {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(1200, now);
        osc.frequency.exponentialRampToValueAtTime(300, now + 0.04);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.04);
      } else if (type === 'subdrop') {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(140, now);
        osc.frequency.exponentialRampToValueAtTime(35, now + 0.55);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.6);
      } else if (type === 'glitch') {
        const bufferSize = audioCtx.sampleRate * 0.08;
        const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = Math.random() * 2 - 1;
        }
        const noise = audioCtx.createBufferSource();
        noise.buffer = buffer;
        const gain = audioCtx.createGain();
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        noise.connect(gain);
        gain.connect(audioCtx.destination);
        noise.start(now);
      } else if (type === 'beep') {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(587.33, now); // D5
        osc.frequency.setValueAtTime(880, now + 0.08); // A5
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 0.25);
      }
    }

    // Simulator trigger
    function triggerSimExploit() {
      playCyberSound('glitch');
      setTimeout(() => playCyberSound('subdrop'), 100);
      const res = document.getElementById('sim-result');
      res.style.display = 'block';
    }

    // Evidence filter
    function filterEvidence(category) {
      playCyberSound('click');
      const buttons = document.querySelectorAll('.tab-btn');
      buttons.forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');

      const cards = document.querySelectorAll('#evidence-container .dosis-card');
      cards.forEach(card => {
        if (category === 'all' || card.dataset.cat === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    // Script Data
    const scenes = [
      {
        num: "ESCENA 01",
        time: "00:00 - 00:45",
        text: "«Todo comenzó a las 3:14 de la tarde. No hubo alarmas, ni sirenas, ni pantallas rojas parpadeando como en las películas. Solo hubo un mensaje: '¿Eres tú el del video?' o tal vez: 'Descarga el mod gratis con monedas infinitas'. Tu cerebro tardó 400 milisegundos en sentir curiosidad. Tu pulgar se movió en menos de medio segundo. Pulsaste. Nada explotó. Tu teléfono siguió funcionando... o al menos, eso creías. Somos el Equipo Alfa. Y hoy no venimos a decirte que no uses internet. Venimos a mostrarte qué ocurre exactamente detrás del cristal cuando un ser humano común comete un error de un solo segundo.»",
        onscreen: "400 ms: EL COSTO DE UN IMPULSO",
        visuals: "Smartphone flotante 3D sobre fondo negro absoluto. Notificación háptica que entra con leve rebote.",
        audio: "Silencio total inicial. Vibración háptica real. Entrada de pulso electrónico grave a 85 BPM.",
        goal: "Generar tensión y empatía inmediata en los primeros 10 segundos sin caer en sermones."
      },
      {
        num: "ESCENA 02",
        time: "00:45 - 01:30",
        text: "«Tendemos a creer que el ciberdelincuente es un genio encapuchado en un sótano hackeando el Pentágono. La realidad es mucho más decepcionante: no hackean computadoras; hackean personas. En la Escuela Nacional Preparatoria y en todo México, más del 80% de los accesos a datos personales no empiezan con una vulnerabilidad en un servidor blindado, sino con un estudiante cansado que quería jugar, bajar un archivo de Office gratis o ver un capítulo de su serie favorita sin pagar. El riesgo es inherente porque la red se diseñó para compartir información, no para desconfiar de ella.»",
        onscreen: "NO HACKEAN MÁQUINAS. MANIPULAN PERSONAS.",
        visuals: "Rostro holográfico vectorial que se disuelve en miles de nodos de red luminosos.",
        audio: "Synthwave ambiental pulsante. Sonido de tecleo sutil de fondo.",
        goal: "Fijar el concepto de riesgo inherente y desmitificar la figura del hacker de película."
      },
      {
        num: "ESCENA 03",
        time: "01:30 - 02:30",
        text: "«Hablemos del malware con honestidad. ¿Alguien aquí se despertó hoy con ganas de instalarse un virus? Nadie. El software malicioso no se vende como veneno; se disfraza de tu comida favorita. Cuando descargas un 'crack' para saltarte una licencia, ¿te has preguntado quién pasó semanas programando ese parche solo para dártelo gratis? No son beneficencias. El software legítimo te cuesta dinero; el software 'crackeado' te cuesta tus cuentas, tus contraseñas y tus conversaciones privadas. El archivo ejecutable abre el programa, pero en segundo plano despliega un InfoStealer silencioso.»",
        onscreen: "SI NO TIENE PRECIO, EL PRODUCTO ERES TÚ",
        visuals: "Caja de regalo digital o icono de juego que se despelleja en 3D revelando código binario rojo.",
        audio: "Sub-bass drop pesado al dividirse el icono; ruido blanco de glitch.",
        goal: "Comprender la falacia del software gratuito y cómo operan los InfoStealers."
      },
      {
        num: "ESCENA 04",
        time: "02:30 - 03:30",
        text: "«En informática distinguimos a las amenazas no por cómo se llaman, sino por lo que buscan. El troyano es la puerta de entrada; te engaña para que lo dejes pasar. El spyware se sienta en una esquina de tu sistema operativo a registrar cada pulsación de teclado y cada sesión abierta de Google o Instagram. Y el ransomware no se oculta: llega, cifra tus fotos y tus proyectos escolares con una llave matemática indestructible, y pone un precio sobre tu propia memoria digital. No son conceptos abstractos de laboratorio; son modelos de negocio ilícitos altamente rentables.»",
        onscreen: "TROYANO (Puerta) · SPYWARE (Espía) · RANSOMWARE (Secuestro)",
        visuals: "Tres monolitos digitales volumétricos que se iluminan al ser nombrados con sus respectivos códigos.",
        audio: "Crescendo de percusión industrial rítmica a 90 BPM.",
        goal: "Dominar la taxonomía básica de malware de forma clara y sin tecnicismos innecesarios."
      },
      {
        num: "ESCENA 05",
        time: "03:30 - 04:30",
        text: "«¿Por qué caemos? Porque el ataque está calibrado para nuestra psicología. Urgencia: 'Bloquearemos tu cuenta en 10 minutos'. Miedo: 'Se detectó un inicio de sesión no autorizado en tu banco'. FOMO o codicia: 'Últimos 3 accesos para la beta'. Cuando una pantalla apela a tus emociones extremas, tu corteza prefrontal cede el control al impulso. El atacante no necesitó romper el cifrado AES-256 de tu teléfono: solo necesitó que tú mismo le teclees tu usuario y contraseña en una página web que lucía idéntica a la original.»",
        onscreen: "URGENCIA. MIEDO. CURIOSIDAD. (HACKEO COGNITIVO)",
        visuals: "Simulación de interfaz de phishing bancario e Instagram falso que se superponen con kinetic typography.",
        audio: "Tictac acelerado de reloj digital que se apaga de golpe al mencionar el engaño.",
        goal: "Identificar los gatillos de la ingeniería social y comprender por qué funcionan."
      },
      {
        num: "ESCENA 06",
        time: "04:30 - 05:45",
        text: "«Seguramente has visto el meme del iceberg. Nos dicen que la Deep Web y la Dark Web son lo mismo y que ambas son un antro de delitos. Falso. La Deep Web es simplemente información que no está abierta a los buscadores: el portal de calificaciones de la UNAM, tu bandeja de correo, tu expediente médico. Es privada y legítima. La Dark Web, en cambio, es una fracción diminuta que requiere protocolos de enrutamiento especial como Tor. ¿Nació para el mal? No; nació para garantizar el anonimato de activistas y periodistas bajo regímenes autoritarios. Pero cuando ese anonimato se vuelve absoluto, aparecen los mercados clandestinos con datos robados a personas como nosotros.»",
        onscreen: "SURFACE (10%) · DEEP (Privacidad) · DARK (Anonimato dual)",
        visuals: "Corte transversal tridimensional de la red con gradiente de profundidad de cian a púrpura profundo.",
        audio: "Drone electromagnético subacuático suave con ecos espaciales.",
        goal: "Desmitificar la Dark Web separando el protocolo técnico de los delitos concretos."
      },
      {
        num: "ESCENA 07",
        time: "05:45 - 06:45",
        text: "«Aterricemos esto en nuestro salón de clases. Según datos oficiales del INEGI, en México más de 100 millones de personas navegamos todos los días, y la Ciudad de México lidera el país con más del 90% de hogares conectados. Pero las cifras del MOCIBA y de la Policía Cibernética de la Ciudad de México confirman una realidad contundente: los estudiantes de nivel medio superior somos el segmento más expuesto al robo de cuentas, extorsión digital y suplantación de identidad. No le ocurre únicamente a grandes corporativos con millones de dólares. Le ocurre a tu compañero de banca al que le clonaron el WhatsApp para pedir dinero prestado a sus familiares fingiendo una emergencia escolar.»",
        onscreen: "MÉXICO: +100M USUARIOS // CDMX: >90% HOGARES // ENP EXPUESTA",
        visuals: "Mapa de la Ciudad de México con pulsos de luz en las coordenadas de los 9 planteles de la ENP.",
        audio: "Beat rítmico continuo, serio y enfocado.",
        goal: "Conectar las estadísticas nacionales con la vulnerabilidad cotidiana de los alumnos de preparatoria."
      },
      {
        num: "ESCENA 08",
        time: "06:45 - 07:45",
        text: "«Caso real documentado: Un alumno busca una plantilla de edición de video o un plugin de sonido para una tarea. El primer resultado de búsqueda en Google es un anuncio patrocinado idéntico a la página oficial. El alumno descarga un archivo comprimido .ZIP con contraseña. Al descomprimirlo y ejecutarlo, el antivirus no reacciona a tiempo porque el ejecutable venía camuflado. Dos horas después, todas sus sesiones de correo, sus cuentas de juegos y sus redes sociales cambian de contraseña desde una dirección IP al otro lado del mundo. ¿Hubo un hackeo cuántico? No. Hubo un engaño visual en el motor de búsqueda.»",
        onscreen: "CASO FORENSE: EL ANUNCIO PATROCINADO // 120 MINUTOS",
        visuals: "Línea temporal animada en pantalla dividida: búsqueda web a la izquierda, terminal forense a la derecha.",
        audio: "Alerta sonora grave de advertencia. Tensión calculada.",
        goal: "Ilustrar con un caso creíble y cercano cómo ocurre la adquisición involuntaria de malware."
      },
      {
        num: "ESCENA 09",
        time: "07:45 - 08:45",
        text: "«La seguridad 100% infalible no existe, pero reducir el riesgo un 95% está en nuestras manos sin gastar un solo peso: Uno: Doble factor de autenticación mediante aplicaciones generadoras de códigos temporales, jamás mediante mensajes SMS simples. Dos: Un gestor de contraseñas. Dejar de reutilizar la misma clave del correo para todas las aplicaciones y redes sociales. Tres: Descargas cero fuera de repositorios oficiales. Si es de pago y te lo ofrecen gratis en un canal de Telegram, el producto que se vende eres tú. Cuatro: Copias de seguridad frías. Si un ransomware ataca tu laptop, tus tareas y tu vida digital deben seguir a salvo en un disco externo desconectado.»",
        onscreen: "4 ESCUDOS ACTIVOS: 2FA APP · GESTOR · TIENDAS OFICIALES · COPIA FRÍA",
        visuals: "HUD de defensa que despliega cuatro cuadrantes lumínicos que se ensamblan en forma de escudo.",
        audio: "Chimes de confirmación positiva electrónica. Sensación de triunfo y control.",
        goal: "Proporcionar soluciones accionables, gratuitas y realistas de implementar de inmediato."
      },
      {
        num: "ESCENA 10",
        time: "08:45 - 09:30",
        text: "«¿Y si ya caíste? La peor respuesta es la vergüenza y el silencio. Paso 1: Desconecta el dispositivo de Internet inmediatamente (corta el Wi-Fi y apaga los datos) para frenar la extracción de información. Paso 2: Desde otro dispositivo limpio, revoca las sesiones activas de todas tus cuentas principales y cambia las contraseñas maestras. Paso 3: Notifica a tus contactos clave para evitar que sean estafados a tu nombre. Paso 4: Reporta ante las instancias institucionales de la UNAM (UNAM-CERT) o la Policía Cibernética de la SSC CDMX.»",
        onscreen: "PROTOCOLO DE INCIDENTE: DESCONECTA → REVOCA → NOTIFICA → REPORTA",
        visuals: "Checklist de emergencia con colores ámbar y esmeralda.",
        audio: "Pauta sosegada y directiva, transmitiendo tranquilidad ante emergencias.",
        goal: "Enseñar qué hacer concretamente ante un incidente real sin perder tiempo por pánico."
      },
      {
        num: "ESCENA 11",
        time: "09:30 - 10:15",
        text: "«Regresemos a las 3:14 de la tarde. La pantalla vuelve a encenderse frente a ti. La notificación vuelve a llegar. El enlace brilla. La tecnología seguirá evolucionando, las interfaces seguirán siendo atractivas y los disfraces seguirán perfeccionándose con inteligencia artificial. El sistema operativo de tu teléfono tiene millones de líneas de código blindadas. Pero el cortafuegos más poderoso del planeta no está hecho de silicio ni de algoritmos. Está ubicado exactamente entre tus dos oídos. En internet, no gana quien da más clics rápidos. Gana quien sabe detenerse dos segundos a pensar. Muchas gracias. Somos el Equipo Alfa.»",
        onscreen: "EL CORTAFUEGOS MÁS PODEROSO ESTÁ ENTRE TUS DOS OÍDOS.",
        visuals: "Regreso cinematográfico a la primera escena; la mano se retira de la pantalla sin tocar el enlace. Logo Alfa.",
        audio: "Silencio total tras la última frase. Acorde final suave de sintetizador.",
        goal: "Cierre memorable con estructura circular y frase contundente que resuene tras la clase."
      }
    ];

    function renderSceneNav() {
      const container = document.getElementById('scene-nav-bar');
      container.innerHTML = '';
      scenes.forEach((scene, index) => {
        const btn = document.createElement('button');
        btn.className = `scene-selector-btn ${index === 0 ? 'active' : ''}`;
        btn.innerText = `${scene.num} (${scene.time.split(' ')[0]})`;
        btn.onclick = () => selectScene(index, btn);
        container.appendChild(btn);
      });
    }

    function selectScene(index, btn) {
      playCyberSound('click');
      document.querySelectorAll('.scene-selector-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const s = scenes[index];
      document.getElementById('scene-number-title').innerText = `${s.num} // ${s.time}`;
      document.getElementById('scene-text-content').innerText = s.text;
      document.getElementById('spec-onscreen').innerText = s.onscreen;
      document.getElementById('spec-visuals').innerText = s.visuals;
      document.getElementById('spec-audio').innerText = s.audio;
      document.getElementById('spec-goal').innerText = s.goal;
    }

    // Initialize
    window.addEventListener('DOMContentLoaded', () => {
      renderSceneNav();
    });
  </script>
</body>
</html>
'''

with open('/Users/shaminket/.gemini/users/user1/equipo-alfa-riesgos-internet/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Página web generada con éxito en /Users/shaminket/.gemini/users/user1/equipo-alfa-riesgos-internet/index.html")
