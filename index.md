<link type="text/css" rel="stylesheet" href="./styles.css">
<div class="mainDetails">
	<div id="headshot" >
			<img src="./anderson_headshot.jpg" alt="Zach Siegel" />
	</div>
	<div id="name">
		<h1 style="margin-bottom : 1px;">Zach Siegel</h1>
		<h2>Software Engineer, Data Scientist</h2>
    <h5>Bulding <a href="https://usecurrent.ai" target="_blank">Current.AI</a> full-time since 2024.</h5>
	</div>
	<div id="contactDetails" >
		<ul>
			<li><a href="mailto:zachary.edmund.siegel@gmail.com" target="_blank">zachary.edmund.siegel@gmail.com</a></li>
			<!-- <li><a href="mailto:zachary.siegel.phd@anderson.ucla.edu" target="_blank">zachary.siegel.phd@anderson.ucla.edu</a></li> -->
			<li><a href="https://github.com/zsiegel92" target="_blank">GitHub</a></li>
			<li><a href="https://www.linkedin.com/in/zach-edmund-siegel" target="_blank">LinkedIn</a></li>
			<!-- <li><a href="https://grouptherenow.com">grouptherenow.com</a></li> -->
			<li><a href="https://zsiegel92.github.io/resume/resume_siegel.html">Resume</a> (<a href="https://zsiegel92.github.io/resume/resume_siegel.pdf">pdf</a>)</li>
		</ul>
	</div>
	<div class="clear"></div>
</div>
<br>

## Research and Software Projects

- Recent Hobby/Open-Source Software Projects
  - (2026) [`clue-llm`](https://github.com/zsiegel92/clue-llm) ([live demo](https://clue-llm.com/blog)) - Stress-testing LLM reasoning through next-token prediction. Generates NP-complete SAT logic puzzles rendered detective-style as "who's the killer?" games. Uses SymPy's SAT solver and asks LLMs solve them. Uses single-token strings for clean confidence measurement, to see if models "know when they're right"/"wrong". Includes experiments with strategic fine-tuning on confident mistakes. Inspired by Ilya Sutskever's claim that predicting the killer in a detective novel requires "a fair amount of reasoning."
  - (2026) [`grouptherenow.com`](https://grouptherenow.com)([GitHub](https://github.com/zsiegel92/group_there)) - Carpool optimization app for teams. NextJS/TypeScript re-implementation of the original GroupThere carpool optimization app (see 2016 entry below), with a Python solver backend deployed on [Modal](https://modal.com) infrastructure. Implements combinatorial optimization subroutine in the **Mojo** programming language; mixed-integer linear program implemented in `glpk`, COIN-OR `cbc`, and Nvidia's [`cuOpt`](https://developer.nvidia.com/cuopt), which runs on GPU.

    > The `cuOpt` solver's massive GPU parallelism becomes optimal at large problem sizes, 100+ riders, see [numerical experiment results](https://github.com/zsiegel92/group_there/blob/main/src/solver/BENCHMARK_RESULTS.md#L0-L1)
  - (2026) [`emoji-recsys`](https://github.com/zsiegel92/emoji-recsys) ([live demo](https://emoji-recsys.vercel.app/), [npm](https://www.npmjs.com/package/emoji-recsys)) - Semantic emoji search for React. Type a word or phrase, get the most relevant emojis back. Uses precomputed embeddings for 1,906 emojis and [all-MiniLM-L6-v2](https://huggingface.co/Xenova/all-MiniLM-L6-v2) via [Transformers.js](https://huggingface.co/docs/transformers.js) for query embedding. Runs entirely in the browser.
  - (2025) [`cuopt-stubs`](https://github.com/zsiegel92/cuopt-stubs) - Python stubs for cuOpt LP/MILP solver. The full cuOpt can only be installed on machines that support Cuda, which excludes MacOS - these stubs support writing cuOpt programs with full type-checking support on MacOS. Stubs auto-generated via MyPy `stubgen`.
  - (2025) [`mojal`](https://github.com/zsiegel92/mojal) - Compile & run Mojo programs on [Modal](https://modal.com). Mojo provides Python interop, so `mojal` deploys Mojo programs serverlessly with GPU access.
  - (2025) [`fzf-ts`](https://github.com/zsiegel92/fzf-ts) - A typescript interface to `fzf` via stdout and temp files. Because every selection CLI should really just be `fzf`.
  - (2025) [`linear_cli`](https://github.com/zsiegel92/linear_cli) - CLI tool for managing Linear issues from the command line. Uses `fzf-ts`. Implementation in Go: [linear-cli-go](https://github.com/zsiegel92/linear-cli-go).
  - (2025) [`taste-lever`](https://github.com/zsiegel92/taste-lever) - Simple one-pass prompt-optimization from human-annotated data.
  - (2024) [`arxiv_html_viewer_sanity_chrome_extension`](https://github.com/zsiegel92/arxiv_html_viewer_sanity_chrome_extension) - Chrome extension to hide the unusable UI surrounding the otherwise-great HTML view in Arxiv.
  - (2024) [FastRPC](https://github.com/zsiegel92/fastRPC) a thin abstraction on top of FastAPI that, along with [`openapi-typescript-sdk-generator`](https://github.com/triggerdotdev/openapi-typescript-sdk-generator), allows for a fully type-safe Typescript SDK to be generated instantly on every save during development. Call Python functions from a fully type-aware TypeScript client with no networking code.
  - (2023) [Capsule](https://github.com/zsiegel92/capsule) ([live app](https://capsulepartner.vercel.app/) on Vercel) - a highly-stylized message sharing system. 100% type-aware full-stack NextJS application (via server actions).

- Graduate Research - [_Data Aggregation and Resource Allocation_ (2021)](https://zsiegel92.github.io/writing_repo/UCLA/polling/data_aggregation.pdf) - [_Pandemic Mitigation Optimization_ (2021)](https://zsiegel92.github.io/writing_repo/UCLA/disaster_mitigation/covid_mitigation.pdf) - [_Fairness, Efficiency, and Feature-Awareness in the Allocation of
  Public Goods_ (2020)](https://zsiegel92.github.io/writing_repo/UCLA/polling/alpha_fairness.pdf)
- Graduate Coursework
  - [Ecological Inference Literature Review](https://zsiegel92.github.io/writing_repo/UCLA/stats203/ecological_inference.pdf)
  - [Worker Safety Management](https://zsiegel92.github.io/writing_repo/UCLA/mgmt298d/dangerous_work.pdf)
  - [Worker Safety Optimization](https://zsiegel92.github.io/writing_repo/UCLA/ee236c/dangerous_work.pdf)
  - [Point Cloud Classification: Literature Review and Reproduction of _Point Net (2016)_](https://zsiegel92.github.io/writing_repo/UCLA/math273/pointnet.pdf)
  - [Facility Location Problems Literature Review](https://zsiegel92.github.io/writing_repo/UCLA/mgmt242/pmedian.pdf)
- Optimizing B'nai Mitzvot Scheduling (2018 & 2019)
  - [Documentation](https://zsiegel92.github.io/mitzvah_writeup/Mitzvah.pdf)
  - [Source code 2018 (for 2021 B'nai Mitzvot)](https://github.com/zsiegel92/mitzvah_scheduler)
  - [Source code 2019 (for 2022 B'nai Mitzvot)](https://github.com/zsiegel92/mitzvah_2022)
  - [Front End Demo](https://mitzvah-scheduler.herokuapp.com/form) (takes up to 15 seconds to load if not opened recently)
- _GroupThere_ Carpool Optimization (2016-17) (see 2026 entry above)
  - [Python/Angular Webapp Source](https://github.com/zsiegel92/poolchat)
  - [MATLAB Version Source](https://github.com/zsiegel92/GroupThere)
- Reproducing predictive policing algorithm with _Los Angeles Community Action Network_ (2016-17)
  - [MATLAB source](https://github.com/zsiegel92/HotspotsInLA)
  - [Whitepaper](https://zsiegel92.github.io/writing_repo/Predpol.pdf)
- _FactoryOfEverything_ Supply Chain Optimization (2016)
  - [Documentation of Optimization Model](https://zsiegel92.github.io/optcentral/parameter_description_optcentral.pdf)
  - [Documentation of Data Processing](https://zsiegel92.github.io/optcentral/Theo_Letter_9-8-2016.pdf)
  - [MATLAB source](https://github.com/zsiegel92/optcentral)
- Undergraduate Research
  - [ _Generative Models and Sparse Coding_ (2014)](https://zsiegel92.github.io/writing_repo/Thesis.pdf)
  - [_Anomaly Detection using Dictionary Learning_ (2013)](https://zsiegel92.github.io/writing_repo/Wavefields_Report_compressed.pdf) ([poster presented at Joint Mathematics Meeting 2014](https://zsiegel92.github.io/writing_repo/wavefield_poster.pdf), awarded _Outstanding Presentation Award_)
  - [_Aquatic Insect Populations' Response to Time-Varying Reproductive Rates_ (2012)](https://zsiegel92.github.io/writing_repo/Aquatic_Insects.pdf)
  - [_Zero-Sum Flows of the Linear Lattice_ (2012)](https://zsiegel92.github.io/writing_repo/Zero_Sum_Flows.pdf)

<!-- ## Visualization -->

<!-- * [Physics Tutorial](https://zsiegel92.github.io/Nikki_B)
* [Web Development Tutorial](https://zsiegel92.github.io/Eitan_S)
* [Python Trouble Tutorial](https://zsiegel92.github.io/evilpython)
* [Interactive Jupyter Notebook (Regression)](http://localhost:8888/notebooks/Math%20Camp%20Assignment%20with%20Slider.ipynb) -->
<!-- * [Juggling](https://zsiegel92.github.io/juggling/) -->
