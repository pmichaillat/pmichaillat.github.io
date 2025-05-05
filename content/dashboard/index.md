---
title: "Automated Business Cycle Dashboard"
tags: ["business cycle", "FERU", "job vacancies", "labor market tightness", "Michez rule", "recession indicator", "recession probability", "recessions", "unemployment", "unemployment gap"]
author: ["Pascal Michaillat","Emmanuel Saez"]
description: "A dashboard with real-time charts on US unemployment rate, vacancy rate, labor market tightness, FERU, unemployment gap, and recession probability."
cover:
    image: "/dashboard.png"
    alt: "US recession probability from dual-threshold Michez rule"
    relative: false
editPost:
    URL: "https://github.com/pmichaillat/pmichaillat.github.io/tree/main/content/dashboard"
    Text: "Source code"
showToc: true
disableAnchoredHeadings: false

---

## US unemployment rate

<iframe src="/dashboard/unemployment.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

The unemployment rate is the number of job seekers divided by the number of labor force participants. It measures the share of the labor force that is unemployed. The numbers of job seekers and labor force participants are both measured by the Bureau of Labor Statistics (BLS) from the Current Population Survey (CPS), which is a large-scale household survey. 

## US vacancy rate

<iframe src="/dashboard/vacancy.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

The vacancy rate is the number of job openings divided by the number of labor force participants. It measures the number of job openings per labor force participant. The number of job openings is measured by the BLS from the Job Openings and Labor Turnover Survey (JOLTS), which is a large-scale firm survey.

## US labor market tightness


<iframe src="/dashboard/tightness.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

Labor market tightness is the vacancy rate divided by the unemployment rate. It measures the number of job openings per job seeker. A tightness of 1 marks full employment, or equivalently labor market efficiency. When tightness is below 1, the labor market is inefficiently slack. When tightness is above 1, the labor market is inefficiently tight.

## US full-employment rate of unemployment (FERU)

<iframe src="/dashboard/feru.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

The full-employment rate of unemployment (FERU) is given by the formula $u^\ast = \sqrt{u \times v}$, where $u$ is the unemployment rate and $v$ is the vacancy rate.  The FERU marks full employment and, by construction, labor market efficiency.

## US unemployment gap

<iframe src="/dashboard/gap.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

The unemployment gap is given by $u - u^\ast$, where $u$ is the unemployment rate and $u^\ast$ is the FERU. The unemployment gap indicates the distance from full employment. A positive gap marks an inefficiently slack labor market. A negative gap marks an inefficiently tight labor market.

## US recession indicator

<iframe src="/dashboard/indicator.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

The recession indicator is the minimum of the Sahm-rule indicator (the increase of the 3-month average of the unemployment rate above its 12-month low) and a vacancy analogue (the decrease of the 3-month average of the vacancy rate below its 12-month high). The Michez rule signals a recession when the indicator crosses the threshold of 0.29pp.

## US recession probability

<iframe src="/dashboard/probability.html" style="width: 100%; aspect-ratio: 16 / 9; border: none;"></iframe>

The recession probability is computed from the dual-threshold extension of the Michz rule. The dual-threshold rule works as follows: values of the indicator between 0.29pp and 0.81pp signal a probable recession; values above 0.81pp signal a certain recession. This dual-threshold extension accounts for uncertainty in the true recession threshold and provides a simple way to nowcast recession risk. The recession probability is the fraction of the 0.29pp–0.81pp band that the indicator has covered.

---

## Download data (CSV)

+ [Unemployment rate](/dashboard/unemployment.csv)
+ [Vacancy rate](/dashboard/vacancy.csv)
+ [Labor market tightness](/dashboard/tightness.csv)
+ [Full-employment rate of unemployment (FERU)](/dashboard/feru.csv)
+ [Unemployment gap](/dashboard/gap.csv)
+ [Recession indicator](/dashboard/indicator.csv)
+ [Recession probability](/dashboard/probability.csv)

---

## References

+ [u* = √uv: The Full-Employment Rate of Unemployment in the United States](https://pascalmichaillat.org/13/) – *Brookings Papers on Economic Activity*, 2024 – This paper obtains the formula for the FERU. The formula implies that the labor market is at full employment whenever there are as many job seekers as job openings ($u = v$); inefficiently tight when there are fewer job seekers than job openings ($u < v$); and inefficiently slack when there are more job seekers than job openings ($u > v$).

+ [Has the Recession Started?](https://pascalmichaillat.org/16/) – *Oxford Bulletin of Economics and Statistics*, 2025 – This paper develops the recession indicator and recession threshold, and computes the recession probability. The Michez rule, based on the recession indicator and threshold, detects recessions faster than the Sahm rule. It is also more robust in that it works between 1929 and 2024, whereas the Sahm rule breaks down before 1960.

## Data sources on FRED

+ [Vacancy level, 2001–present](https://fred.stlouisfed.org/series/JTSJOL)
+ [Unemployment level, 1948–present](https://fred.stlouisfed.org/series/UNEMPLOY)
+ [Labor force level, 1948–present](https://fred.stlouisfed.org/series/CLF16OV)

## BLS resources

+ [CPS homepage](https://www.bls.gov/cps/home.htm)
+ [CPS documentation](https://www.bls.gov/cps/documentation.htm)
+ [Latest CPS data release](https://www.bls.gov/news.release/empsit.nr0.htm)
+ [JOLTS homepage](https://www.bls.gov/jlt/)
+ [JOLTS documentation](https://www.bls.gov/jlt/jltfaq.htm)
+ [Latest JOLTS data release](https://www.bls.gov/news.release/jolts.nr0.htm)

---

{{< lastmod >}}

