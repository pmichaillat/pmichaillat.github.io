---
title: "Automated Business Cycle Dashboard"
# date: 2025-05-02
tags: ["business cycle", "FERU", "job vacancies", "labor market tightness", "Michez rule", "recession indicator", "recession probability", "recessions", "unemployment", "unemployment gap"]
author: ["Pascal Michaillat","Emmanuel Saez"]
description: "This webapge hosts an interactive dashboard with real-time charts on US unemployment rate, vacancy rate, labor market tightness, FERU, unemployment gap, recession indicator, and recession probability. Updated daily using FRED data."
cover:
    image: "dashboard.png"
    alt: "US recession probability from dual-threshold Michez rule"
    relative: false
editPost:
    URL: "https://github.com/pmichaillat/pmichaillat.github.io/tree/main/content/dashboard"
    Text: "Source code"
showToc: true
disableAnchoredHeadings: false

---

## US labor market data

<iframe src="/dashboard/unemployment.html" width="100%" height="600" style="border:none;"></iframe>

<iframe src="/dashboard/vacancy.html" width="100%" height="600" style="border:none;"></iframe>

<iframe src="/dashboard/tightness.html" width="100%" height="600" style="border:none;"></iframe>

---

## Deviation of US labor market from full employment


<iframe src="/dashboard/feru.html" width="100%" height="600" style="border:none;"></iframe>

<iframe src="/dashboard/gap.html" width="100%" height="600" style="border:none;"></iframe>

---

## US recession detection by Michez rule


<iframe src="/dashboard/indicator.html" width="100%" height="600" style="border:none;"></iframe>

<iframe src="/dashboard/probability.html" width="100%" height="600" style="border:none;"></iframe>

---

## References

+ [Has the Recession Started?](https://pascalmichaillat.org/16/) – *Oxford Bulletin of Economics and Statistics*, 2025
+ [u* = √uv: The Full-Employment Rate of Unemployment in the United States](https://pascalmichaillat.org/13/) – *Brookings Papers on Economic Activity*, 2024

---

## Data sources

+ [Vacancy level, 2001–present](https://fred.stlouisfed.org/series/JTSJOL)
+ [Unemployment level, 1948–present](https://fred.stlouisfed.org/series/UNEMPLOY)
+ [Labor force level, 1948–present](https://fred.stlouisfed.org/series/CLF16OV)

---

## Bureau of Labor Statistics resources

+ [Latest JOLTS data release](https://www.bls.gov/news.release/jolts.nr0.htm)
+ [Latest CPS data release](https://www.bls.gov/news.release/empsit.nr0.htm)
+ [JOLTS documentation](https://www.bls.gov/jlt/jltfaq.htm)
+ [CPS documentation](https://www.bls.gov/cps/documentation.htm)

---

##### {{< lastmod >}}

