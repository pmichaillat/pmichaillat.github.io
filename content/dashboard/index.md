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

The unemployment rate is the number of job seekers divided by the number of labor force participants. It measures the share of the labor force that is unemployed. The numbers of job seekers and labor force participants are both measured by the US Bureau of Labor Statistics (BLS) from the Current Population Survey (CPS), which is a large-scale household survey. 

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

## Frequently asked questions

#### When do the numbers for the current month become available?

The unemployment and vacancy data required to apply the Michez rule in any given month are released in the first week of the following month, usually [on a Tuesday for the JOLTS data and on a Friday for the CPS data](https://www.bls.gov/schedule/2025/home.htm). Accordingly, the dashboard will generally provide a complete picture for the current month on the first Friday of the following month.

To best align labor force and vacancy data, we shift forward by one month the number of job openings from JOLTS. For instance, we assign to December 2023 the number of job openings that the BLS assigns to November 2023. The motivation for this shift is that the number of job openings from the JOLTS refers to the last business day of the month (Thursday 30 November, 2023), while the civilian labor force from the CPS refers to the Sunday--Saturday week including the 12th of the month (Sunday 10 December 2023 to Saturday 16 December 2023). So the number of job openings refers to a day that is closer to the next month's CPS reference week than to the current month's CPS reference week. 

This is another advantage of shifting forward by one month the number of job openings reported in the JOLTS: we have access to the vacancy and unemployment rates required to compute the minimum indicator in the same week, as soon as the month is over. 

#### Are the numbers final upon release? Or will they be revised?

The value of the variables constructed in real time might not be final because the unemployment, vacancy, and labor force data are revised after their initial release. 

The number of job openings released by the BLS is preliminary and updated one month after its initial release, to incorporate additional survey responses received from businesses and government agencies and from the recalculation of seasonal factors. 

Additionally, the BLS revises the prior five years of CPS and JOLTS data each year at the beginning of January, to account for revisions to seasonal factors, population estimates, and employment estimates. 

Yet, revisions to labor market data are generally minimal, especially compared to GDP revisions, so the information provided in real time is [almost indistinguishable from the information provided in the final version](https://libertystreeteconomics.newyorkfed.org/2020/02/reading-the-tea-leaves-of-the-us-business-cyclepart-one/).

#### Is the vacancy rate inflated by ghost job postings?



### Is the FERU the same as the NAIRU?

#### Is the FERU the same as the NAIRU?

##### Is the FERU the same as the NAIRU?

No. In recent times, the US government has used the non-accelerating-inflation rate of unemployment (NAIRU) as full-employment target. For instance, the [Joint Economic Committee recently wrote](https://perma.cc/E9V8-XTFH):

> Today, full employment is considered by many to be synonymous with the non-accelerating inflationary rate of unemployment (NAIRU)—the rate of unemployment that neither stokes nor slows inflation.

Similarly, the [Council of Economic Advisers described](https://perma.cc/2JGM-QG4Z) the concept of full employment as follows: 

> Modern economics has generally defined full employment by citing the theoretical concept of the lowest unemployment rate consistent with stable inflation, which is referred to as $u^*$, the non-accelerating inflationary rate of unemployment (termed NAIRU).

These quotes are particularly meaningful because the Joint Economic Committee and Council of Economic Advisers were both created by the Employment Act of 1946 to ensure that the government achieved its full-employment mandate.

But this is a misconception. The NAIRU is the unemployment rate at which inflation remains stable. Although the NAIRU contains information relevant to the Fed's price-stability mandate, it does not represent the efficient rate of unemployment \citep[p.~90]{R97}. In modern models of the labor market, workers and firms meet through a matching function and form long-term employment relationships \citep{P00}. In these models, infinitely many real wages are acceptable in equilibrium \citep{H05}. However, only one of those wages yields the efficient rate of unemployment. There is no guarantee that the real wage arising under stable inflation coincides with this efficient real wage \citep{BG10}. Accordingly, there is no guarantee that the unemployment rate prevailing under stable inflation---the NAIRU---is efficient. Since we have defined full employment as a socially efficient allocation of labor, the NAIRU cannot be a measure of full employment.

#### Is the FERU the same as the NRU computed by CBO?



#### Isn't the FERU set by law?



#### Shouldn't the FERU be fixed, just like the inflation target of 2%?



---

## References

+ [u* = √uv: The Full-Employment Rate of Unemployment in the United States](https://pascalmichaillat.org/13/) – *Brookings Papers on Economic Activity*, 2024 – This paper obtains the formula for the FERU. The formula implies that the labor market is at full employment whenever there are as many job seekers as job openings ($u = v$); inefficiently tight when there are fewer job seekers than job openings ($u < v$); and inefficiently slack when there are more job seekers than job openings ($u > v$).

+ [Has the Recession Started?](https://pascalmichaillat.org/16/) – *Oxford Bulletin of Economics and Statistics*, 2025 – This paper develops the recession indicator and recession threshold, and computes the recession probability. The Michez rule, based on the recession indicator and threshold, detects recessions faster than the Sahm rule. It is also more robust in that it works between 1929 and 2024, whereas the Sahm rule breaks down before 1960.

## Data sources on FRED

+ [Number of job seekers, 1948–present](https://fred.stlouisfed.org/series/UNEMPLOY)
+ [Number of labor force participants, 1948–present](https://fred.stlouisfed.org/series/CLF16OV)
+ [Number of job openings, 2001–present](https://fred.stlouisfed.org/series/JTSJOL)

## BLS resources

+ [Latest CPS data release](https://www.bls.gov/news.release/empsit.nr0.htm)
+ [Latest JOLTS data release](https://www.bls.gov/news.release/jolts.nr0.htm)
+ [CPS homepage](https://www.bls.gov/cps/home.htm)
+ [CPS documentation](https://www.bls.gov/cps/documentation.htm)
+ [JOLTS homepage](https://www.bls.gov/jlt/)
+ [JOLTS documentation](https://www.bls.gov/jlt/jltfaq.htm)


---

{{< lastmod >}}

