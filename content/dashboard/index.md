---
title: "Automated Business Cycle Dashboard"
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

## US unemployment rate

The unemployment rate is the number of job seekers divided by the number of labor force participants. The numbers of job seekers and labor force participants are both measured by the [Bureau of Labor Statistics](https://www.bls.gov/) (BLS) from the [Current Population Survey](https://www.bls.gov/cps/home.htm) (CPS). 

<iframe src="/dashboard/unemployment.html" width="100%" height="600" style="border:none;"></iframe>

## US vacancy rate

The vacancy rate is the number of job openings divided by the number of labor force participants. The number of job openings is measured by the BLS from the [Job Openings and Labor Turnover Survey](https://www.bls.gov/jlt/) (JOLTS).

<iframe src="/dashboard/vacancy.html" width="100%" height="600" style="border:none;"></iframe>

## US labor market tightness


The labor market tightness is the vacancy rate divided by the unemployment rate. A tightness of 1 marks full employment, or equivalently labor market efficiency. When tightness is below 1, the labor market is inefficiently slack. When tightness is above 1, the labor market is inefficiently tight. In other words, the labor market is at full employment whenever there are as many job seekers as job openings ($u = v$); inefficiently tight when there are fewer job seekers than job openings ($u < v$); and inefficiently slack when there are more job seekers than job openings ($u > v$).

<iframe src="/dashboard/tightness.html" width="100%" height="600" style="border:none;"></iframe>

## US full-employment rate of unemployment (FERU)


The full-employment rate of unemployment (FERU) is given by the formula $u^\ast = \sqrt{uv}$. The FERU marks full employment and, by construction, labor market effiency.

<iframe src="/dashboard/feru.html" width="100%" height="600" style="border:none;"></iframe>


## US unemployment gap

The unemployment gap simply indicates the distance from full employment. The gap is given by $u - u^\ast$. A positive gap marks an inefficiently slack labor market. A negative gap marks an inefficiently tight labor market.

<iframe src="/dashboard/gap.html" width="100%" height="600" style="border:none;"></iframe>

## US recession indicator

The recession indicator is the minimum of the Sahm-rule indicator (the increase of the 3-month trailing average of the unemployment rate above its 12-month low) and a vacancy analogue (the decrease of the 3-month trailing average of the vacancy rate below its 12-month high). The Michez rule signals a recession when the indicator reaches 0.29pp.


<iframe src="/dashboard/indicator.html" width="100%" height="600" style="border:none;"></iframe>

## US recession probability

The recession probability is computed from the dual-threshold extension of the Michz rule. The dual-threshold rule works as follows: values of the indicator between 0.29pp and 0.81pp signal a probable recession; values above 0.81pp signal a certain recession. This dual-threshold extension accounts for uncertainty in the true recession threshold and provides a simple way to nowcast recession risk. Then, the recession probability is the fraction of the 0.29pp–0.81pp band that the indicator has covered.

<iframe src="/dashboard/probability.html" width="100%" height="600" style="border:none;"></iframe>


---

## References


+ [u* = √uv: The Full-Employment Rate of Unemployment in the United States](https://pascalmichaillat.org/13/) – *Brookings Papers on Economic Activity*, 2024 – This paper obtains the formula for the FERU.

+ [Has the Recession Started?](https://pascalmichaillat.org/16/) – *Oxford Bulletin of Economics and Statistics*, 2025 – This paper develops the recession indicator and computes the recession probability.

## Data sources

+ [Vacancy level, 2001–present](https://fred.stlouisfed.org/series/JTSJOL)
+ [Unemployment level, 1948–present](https://fred.stlouisfed.org/series/UNEMPLOY)
+ [Labor force level, 1948–present](https://fred.stlouisfed.org/series/CLF16OV)

## Bureau of Labor Statistics resources

+ [Latest JOLTS data release](https://www.bls.gov/news.release/jolts.nr0.htm)
+ [Latest CPS data release](https://www.bls.gov/news.release/empsit.nr0.htm)
+ [JOLTS documentation](https://www.bls.gov/jlt/jltfaq.htm)
+ [CPS documentation](https://www.bls.gov/cps/documentation.htm)

---

{{< lastmod >}}

