---
numbering:
  heading_2: false
  figure:
    template: Fig. %s
---

## Introduction


Neurostimulation can be applied on a large panel of nervous system (NS) disorders and injuries by modulating motor, sensory and cognitive functions through electrical stimulation. This technology offers, amongst others, a promising method to restore motor functions in patients living with paralysis due to neurotrauma, with strong potential for enhanced efficacy through improved spatiotemporal precision @ting2021neurostimulation, @james2018neuromodulation.
Neuromodulation systems are becoming increasingly complex @schupbach2017directional, @anderson2018optimized, and this trend is expected to continue and scale further in the future @de2021future. Advances in manufacturing, such as the miniaturization of electrodes enabling higher spatial selectivity, the development of biocompatible designs for targeting areas closer to the nervous system, and the integration of wireless systems providing greater freedom of movement, are key drivers of this evolution @won2020emerging,@jun2017fully, @tsai2017very. These advancements also open the door to interactions with more natural outputs. Whether in large channel-count or smaller devices such as current clinical deep brain stimulation (DBS) leads, the effectiveness of neuromodulation depends on system identification and on fine-tuning numerous control parameters to meet individual needs, problems that advanced optimization algorithms have the potential to solve more efficiently than traditional approaches. 


### A.I. In neurostimulation optimization

A wide range of pre-clinical studies, including on epilepsy @pineau2009treating and Parkinson's disease @gao2023offline, are actively exploring how to enhance neuromodulation results using diverse machine learning (ML) methods such as decision trees @gebodh2021novel, @de2021predictive, random forests @gebodh2021novel, @shukla2014towards, neural networks (NN) @gebodh2021novel, @shukla2012neural, support vector machines (SVM) @gebodh2021novel,, @de2021predictive, @medaglia2020personalizing and Reinforcement Learning (RL) @pineau2009treating, @gao2023offline, @yu2021reinforcement. However, those ML methods rely on pre-training and require a huge number of iterations to converge to a solution, making them impractical to use in an online context. Online neurostimulation optimization means in vivo trial-and-error tuning of a neural interface, where decisions involve selecting from a large number of parameter options, and the constantly evolving environment induces both noise and non-stationarity in the response.  

To date, real-time neurostimulation optimization in clinical studies is performed by adaptive stimulation @arlotti2018eight, @rosa2015adaptive, @swann2018adaptive. This closed-loop method traditionally relies on turning on and off DBS and varying the amplitude based on neurophysiological feedback, but this approach is not tailored for a complex multivariate problem such as selecting what specific stimulation pattern to activate, among an immense number of options for varying contact, frequency, current amplitude and pulse width. To offer a solution adapted to optimization of multi parameters, some studies focus on a class of algorithms that does not require training and that relies on parametric models of stimulation properties. Bayesian Optimization based on Gaussian Process (GPBO) can offer an effective solution @bonizzato2023autonomous, @choiniere2024gaussian, @laferriere2020hierarchical, @sarikhani2022automated, @aiello2023recalibration. GPBO tests single-input parameter combinations (“queries”), leveraging responses to build an evidence-based approximation (“surrogate” function) that describes how stimulus choices affect the desired output. This approach allows to efficiently explore high dimensional spaces in a small number of iterations. 


### Optimizing stimulation for movement disorders

Restoring motor control after neurotrauma or in disease is a very complex neuromodulation challenge since the movement is controlled by distributed brain and spinal networks with variable dynamic states and outputs. Promising studies already show how advanced optimization methods can enhance mobility @bonizzato2023autonomous, @grahn2014restoration, @losanno2021bayesian, but the field of motor neuroprosthetics is still young. Novel exciting demonstrations of motor control restoration feature complex neuroprosthetic systems, with a high degree of control complexity @rowald2022activity, @wagner2018targeted. Research to develop optimization agents to fine-tune such systems once they are implanted largely benefits from offline modeling and simulation @bonizzato2023autonomous, @capogrosso2013computational.

To effectively train and test complex ML models or simulate online experimental neurostimulation sessions, a diverse range of neurostimulation datasets is essential @wang2023machine, @bonizzato2023autonomous. Such datasets must account for variability across subjects, species, and neural interface targets. For example, rodents provide the advantage of generating large datasets due to relatively restrained costs, while NHPs offer a closer approximation to human brain complexity, making both species invaluable for research. The characteristics of any single dataset can vary widely due to environmental factors and experimental design, leading to significant differences not only between rodent and NHP data but also across neural targets such as the spinal cordspinal cord and cortex—even within subjects of the same species. Ensuring algorithm robustness across this variability is essential for preclinical and clinical applications.

Although synthetic data can serve as an initial benchmark for algorithm performance, it falls short in addressing the complexities inherent to in vivo data. Many neurophysiological mechanisms, such as the biological variability of motor responses, remain poorly modeled. This variability causes, among other things, inconsistencies in neural output to identical stimulation parameters and is compounded by noise introduced by experimental setups. These challenges make in vivo validation important, not only for assessing algorithm functionality but also for uncovering patterns of responses to neural stimuli and deepening our understanding of neural circuits response dynamics and non-stationarities. However, expanding the collection of neurostimulation datasets faces significant barriers, including high costs, technical complexity, and ethical considerations.
The recent surge in optimization algorithms within this field opens new possibilities for neurostimulation applications. To further push the boundaries of AI in neurostimulation, it is essential to broaden the dataset pool, thereby supporting a wider range of innovative use cases.

Our goal is to develop NeuroMOSAICS (Neurostimulation Multi-scale Open-Source Across Interface, Conditions & Species), a collection of open-access datasets comprising a wide range of different neurostimulation scenarios: in rats and non-human primates (NHP), in sedated and awake animals, in intact and injured subjects, in small and large input spaces optimization, and in both cortical and spinal neurostimulation interventions. NeuroMOSAICS aims to support the development of neurostimulation optimization algorithms. This collection is an attempt to regroup and valorize all neurostimulation characterization datasets opened by the community. This collaborative effort would not only allow the training and testing of data-demanding algorithms, but also make valuable knowledge accessible to a broader audience, thereby encouraging the ML community to develop algorithms suited to neurostimulation problems. 

This living white paper intends to evolve in time with new incoming open-source datasets. New datasets will be added as we target additional unmet needs in neurostimulation optimization. Moreover, we aim to incorporate complex datasets that establish benchmarks and open avenues for novel algorithmic solutions. Datasets may also be introduced in response to community demand or as invited contributions. We welcome opportunities to review contributions from groups exploring high-dimensional optimization, to collaboratively grow this evolving body of work. 

## Material and method 

In this section we describe how each featured dataset has been collected. We wrote this section with a focus on clarity and a level of readership accessible to those without a background in neuroscience.

### Dataset 1 – forelimb muscle responses to cortical stimulation in NHP and rats

**Input:** coordinates of an electrode in a 96 electrodes array for NHP and 32 electrodes array for rats.  
**Output:** Motor Evoked Potentials (MEPs) from 4 to 8 arm, forearm and hand muscles.  
**Replicates:** Data were collected from N=4 NHP and N=6 rats (biological replicate). For each independent muscle, technical replicates ranged from 10 to 28 repetitions.  
**Depth:** The same neurostimulation is repeated 10 to 28 times per site (muscle) per subject, resulting in an equivalent number of MEP measurements being collected. Each MEP represents the muscle response within a time window of -100 to 200 ms relative to the stimulation delivery (0 ms).  
**Rationale:** to develop optimization algorithms to efficiently optimize neurostimulation within a set of electrode location options.  

This dataset contains forelimb EMG responses to cortical stimulation in 4 male NHPs (2 macaques, 2 capuchins) and 6 female rats. The dataset, available on OSF, was collected to develop a Gaussian Process Bayesian Optimization (GPBO) framework, an algorithm designed to optimize neurostimulation parameters for maximizing MEPs. Cross-species data can challenge the robustness and adaptability of optimization algorithms, testing their ability to generalize across scales and from simpler to more complex cortical organizations, that approximate better the human brain. 

The detailed protocol for surgery and experiment is available on M. Bonizzato et al. @bonizzato2023autonomous, @choiniere2024gaussian.
The rats were implanted with 32-microelectrode arrays in the hindlimb sensorimotor cortex and the NHPs were implanted with 96-electrode arrays implanted in the hand area of the primary motor cortex (M1). For both rats and NHPs, the EMGs were implanted in forelimb muscles. When the stimulation protocol was running, the two capuchin NHP were under sedation and the two macaques were awake.

### Dataset 2 – forelimb muscle responses to spinal stimulation in rats

**Input:** coordinates of an electrode in a 64 electrodes array.  
**Output:** motor evoked potentials from 8 to 10 arm muscles.  
**Replicates:** Data were collected from N=4 rats (biological replicate). For each independent muscle, technical replicates ranged from 10 to 15 repetitions.   
**Depth:** The same neurostimulation is repeated 10 to 15 times per site (muscle) per subject, resulting in an equivalent number of MEP measurements being collected. Each MEP represents the muscle response within a time window of -35 to 40 ms relative to the stimulation delivery (0 ms).   
**Rationale:** to develop optimization algorithms to efficiently optimize neurostimulation within a set of electrode location options and multiple concurrent output muscle objectives (8-10 bilateral and varied agonist/antagonist muscles).

This dataset contains EMG responses to spinal cord stimulation in the forelimbs of 4 female Long Evans rats. EMG electrodes were implanted bilaterally in the Biceps, Triceps, Flexor Carpi Radialis, Deltoid, and Dorso muscles. spinal cord stimulation was delivered via a 64-electrode array placed epidurally.

<u>Experiment Description</u>

A 64-electrode array was placed epidurally on the spinal cord (C3-C7) of four sedated rats. Up to three placements of the array were tested in this region. EMG activity was recorded from muscles in both forelimbs in response to stimulation.

<u>Surgical Procedure</u>

The experiments were terminal. Rats were anesthetized with urethane (1 g/kg) prior to surgery. After 30 minutes, they were transitioned to isoflurane anesthesia (∼2%). Isoflurane was withdrawn prior to stimulation, and the rat maintained under the initial dose of urethane. Vital signs, temperature, and hydration were continuously monitored.

*EMG Implants*
EMG microwires were implanted in the Biceps, Triceps, Flexor Carpi Radialis, Deltoid, and Dorso muscles on both sides. Correct placement was confirmed by electrical stimulation through the wires and observation of evoked movements. Wires were inserted transcutaneously.

*Spinal Cord Implants*
The dura mater was exposed from C3 to C6. Initially, a single electrode was used to determine muscle response thresholds. A 64-electrode array was then placed epidurally at up to three different locations.

<u>Data Collection</u>

For each placement, 10 repetitions of single-pulse stimulation were delivered to each electrode in random order using Tucker-Davis Technologies (TDT) equipment. Stimulation amplitude was set to the threshold value identified during single-electrode testing.

*Suggestion of processing*
The filtered signal given additionally in this dataset has been (in the following order):
-	High-passed at 70Hz;  
-	Blanked from electrical artefact;  
-	Bandpassed;  
-	Rectified.  

## Results

In this section, we frequently refer to the heatmaps in each Figure. Each heatmap corresponds to a specific muscle from a subject and displays the average quantification of motor evoked potentials (MEPs) across different electrodes. Those electrode arrays allow us to map the topographic organization of the implanted motor region. Typically, the best-performing electrodes cluster spatially. Each query refers to an individual stimulation.

### Dataset 1

Dataset 1 was collected during in vivo sessions that involved repeated stimulations of electrode locations in M1. These stimulation sessions were initially conducted on sedated capuchins and on awake rats and macaques. The average MEP responses across spatial locations show a topographic organization of M1 such that nearby cortical locations have similar MEP patterns [Figure Cebus Part 1]. While identifying the optimal electrode in this condition may seem straightforward, it presents significant challenges. First, the heatmaps represent averages of MEP, but individual responses are influenced by excitability, noise factors, and possibly non-stationarity, leading to considerable variability[Figure Cebus Part 2]. Given the goal of minimizing the number of queries, the task becomes finding the right balance between using enough queries for a robust solution and limiting the search to minimize stimulation.

:::{figure} #figCebcell
:label: figMcqcell
**A.  Heatmap of Motor Responses Across a 96-Electrode Array in M1 of an anesthetized Cebus:** This panel displays the mean motor responses for a selected muscle, averaged across repetitions, for each electrode in a 96-electrode array (10x10 grid with 4 unused electrodes). To view data for a specific muscle, select the desired muscle from the list on the right. The available muscles are: Flexor Carpi Ulnaris (FCU), Extensor Digitorum Communis (EDC), Extensor Carpi Radialis (ECR), Opponens Pollicis (OP), Flexor Pollicis Brevis (FPB), and Adductor Pollicis (AP).
**B.  Detailed Motor Evoked Potential (MEP) Response for a Single Electrode:** This panel provides detailed visualizations for the MEP response corresponding to a selected electrode from the heatmap in A (click on the corresponding cell to select it).
- *Top Left:* The mean MEP waveform across all repetitions.
- *Top Right:* The distribution of peak amplitudes for the selected electrode.
- *Bottom Left:* A stack plot showing the rectified raw MEP waveforms for individual repetitions. Red color hilights outliered trials.
:::
The clear topographic organization of the responses observed in sedated NHPs become considerably noisier and more selective in awake NHPs [Figure Macaque Part 1]. These NHP implants were older, and the quality of the electrical interface at the EMG wire-muscle contact can degrade over time, potentially contributing to variations in noise levels in the recorded muscle responses across subjects. Additionally, the NHPs were awake, which may have further contaminated MEPs with spontaneous muscle activations, which are possibly present even when the condition of no muscle activity pre-stimulation is enforced. Consequently, this dataset provides an opportunity to test optimization approaches on data that differ significantly from the previous dataset.

:::{figure} #figMcqcell
:label: figMcqcell
**A.  Heatmap of Motor Responses Across a 96-Electrode Array in M1 of an awaken Macaque:** This panel displays the mean motor responses for a selected muscle, averaged across repetitions, for each electrode in a 96-electrode array (10x10 grid with 4 unused electrodes). To view data for a specific muscle, select the desired muscle from the list on the right. The available muscles are: First Dorsal Interosseous (FDI), Flexor Digitorum Superficialis (FDS), Extensor Carpi Radialis (ECR), Extensor Digitorum Communis (EDC).
**B.  Detailed Motor Evoked Potential (MEP) Response for a Single Electrode:** This panel provides detailed visualizations for the MEP response corresponding to a selected electrode from the heatmap in A (click on the corresponding cell to select it).
- *Top Left:* The mean MEP waveform across all repetitions.
- *Top Right:* The distribution of peak amplitudes for the selected electrode.
- *Bottom Left:* A stack plot showing the rectified raw MEP waveforms for individual repetitions. Red color hilights outliered trials.
:::
High selectivity becomes particularly problematic when the search space is expanded (such as by adding additional parameters like stimulation amplitude and frequency) and even more so in noisy conditions. If it makes it harder to identify the best electrode, the global maximum of the function to optimize, and increases the risk of getting stuck in local maxima during optimization. For example, while searching for the electrode that grants maximal response in the First Dorsal Interosseous muscle [Figure Macaque Part1], one could easily get stuck at coordinates (7,7) on the heatmap. If the algorithm hasn’t yet queried the optimal electrode at coordinates (4,1), and instead queries (7,7) at a given query q, it will produce the best result thus far. The algorithm would then continue to exploit the local maximum around (7,7) without knowing that a better option exists unless it explores very specific electrodes (4,1) or (5,1) [Figure Macaque Part 2]. With around 50 electrodes to query in a limited number of stimulations, the algorithm's exploration strategy becomes critical to avoid local maxima. This issue of local maxima and high selectivity is also observed in awake rats, as seen in the Left Medial Gastrocnemius available in Dataset 1 on OSF. However, the smaller array (32 electrodes, compared to 96 for NHPs) reduces the complexity of the search.

The temporal aspect of the responses can play an important role in the nature of the response. In any scenario from this dataset, the stronger stimuli MEP are peaking at the same time as we can observe in the stacked MEP where deeper blue lines are vertically crossing all the trials. 
Considering noise (such as muscle activations unrelated to stimulation), some responses may convey misleading information about the overall response pattern. Identifying these outliers in real time is challenging, but it is valuable to do so afterward as it raises awareness of their potential impact on optimization processes. The parameter is_valid classifies outliers in two categories: those that can be excluded due to excessive EMG activity prior to stimulation and those that cannot be excluded, where no prior EMG activity was observed, but the response amplitude is unusually high. Accurate online processing can easily reject the first of the two classes, while the second is unlikely to be rejected in a real use case. The first category is highlighted in red in the stack MEP figures. The mean and standard deviation of responses in Dataset 1 still include these outliers. A data scientist wishing to remove these spurious responses from the optimization “ground truth”, or objective value, must though recalculate the mean responses.

### Dataset 2

This dataset was collected from four sedated rats, resulting in smooth topographic organization of the spinal cord with high variance for the average responses. Similar to capuchin in Dataset 1, the relaxed muscle state in sedated animals, with no intention of motor control or reflex interference, contributes to the smooth responses. However, unlike Dataset 1, this dataset involves spinal cord (spinal cord) stimulation, leading to some key differences in the results. One notable distinction is the spreader cluster of best electrodes, which may be attributed to the different recruitment of spinal cord stimulation compared to motor cortex stimulation.  Because dorsal spinal cord stimulation is closer to the muscle target than M1 stimulation, there is less variability in the responses. Indeed, less synapses (and thus less pulses) lead to a higher repeatability of the responses. This very clear repeatability (a straight deep blue line across each trial in stack MEP figures) makes the identification of outliers easier, and they are also listed in a parameter is_valid and highlighted in red in the stack MEP figures. In this case, the mean and the standard deviation were computed without those outliers.

:::{figure} #figRatcell
:label: figRatcell
**A.  Heatmap of Motor Responses Across a 64-Electrode Array in M1 of an anesthetized Rat:** This panel displays the mean motor responses for a selected muscle, averaged across repetitions, for each electrode in a 64-electrode array (8x8 grid with 4 unused electrodes). To view data for a specific muscle, select the desired muscle from the list on the right. The available muscles are: Right Triceps (R Tr), Right Biceps (R Bi), Right Torso (R Trs), Right Wrist flexor (R WrFlex), Right Spinal Deltoid (R SpDel), Left Triceps (L Tr),
Left Biceps (L Bi), Left Tors (L Trs), Left Wrist flexor (L WrFlex), Left Spinal Deltoid (L SpDel).
**B.  Detailed Motor Evoked Potential (MEP) Response for a Single Electrode:** This panel provides detailed visualizations for the MEP response corresponding to a selected electrode from the heatmap in A (click on the corresponding cell to select it).
- *Top Left:* A stack plot showing the rectified raw MEP waveforms for individual repetitions. Red color hilights outliered trials.
- *Top Right:* A stack plot showing the filtered MEP waveforms for individual repetitions.
- *Bottom Left:* The mean MEP waveform across all repetitions. 
- *Bottom Right:* The distribution of peak amplitudes for the selected electrode.
:::

When the clear repeatability from this dataset has a positive impact on the optimization process, the excitability and noise can be, in some cases, particularly challenging. Indeed, the excitability can increase and decrease drastically in a few queries (like for electrode (2,4) in Left Biceps [Figure rat Part 2]), and some electrodes are losing contact on half of the process (like in electrode (4,3) in Left Biceps), making it harder to identify a best electrode and to take a decision on the definition of what is the best electrode. This phenomenon highlights potential future use of this dataset to take into account the non-stationarity of the responses.

The higher variance in this dataset tends to blur the distinction between the best average solution and its neighboring electrodes. This makes it easy to identify the best location area, but also more challenging to point out the precise optimal electrode. As the variance of the GD increases, so does the likelihood that, at query q, the response from the best electrode is worse than those of nearby electrodes. For instance, in the Right Biceps muscle [Figure rat Part 1], the peak amplitude distribution from the best electrode (coordinates (2,5)) is centered at 13.1 mV, but there is an outlier stimulation yielding a response of 11.2 mV. Meanwhile, the electrode at coordinates (2,4) has stimulations with outputs around 13.1 mV. If an algorithm repeatedly queries electrode (2,4) and obtains consecutively good motor responses, while a single query of electrode (2,5) produces an outlier of 11.2 mV, the algorithm might incorrectly infer that electrode (2,4) is superior. Although (2,4) is not the global maximum, it remains a strong candidate because it provides stable, high-quality responses and is situated within the highest region of the heatmap. This example also illustrates the difficulty to identify the criteria for choosing the best electrode, such as the best mean response or less variability.  

Another key insight from this dataset is the spatial organization of the spinal cord for motor control. There is a clear lateralization, with the right side of the spinal cord predominantly evoking stronger responses in muscles on the right side of the body, and the left side evoking responses in left-side muscles. Additionally, there appears to be spatial clustering in spinal cord sites evoking motor potential in specific muscles. The spatial organization is non-trivial given that the dorsal aspect of the spinal cord, which we stimulated, is associated with afferent pathways, and motor output depends on reflex responses @capogrosso2013computational. This insight has significant implications for optimization in neuromodulation. The function linking stimulation parameters to motor responses is inherently complex and unknown, posing a "black-box" optimization problem. In order to facilitate the optimization task, incorporating prior knowledge about the spatial organization of the spinal cord can significantly enhance the efficiency of optimization algorithms, such as BO, that is designed to leverage prior information to reduce the complexity of the search space and accelerate convergence to optimal solutions @greenhill2020bayesian. For example, integrating the knowledge that stimulating the left (or right) dorsal spinal cord enhances motor responses on the corresponding side of the body allows the algorithm to narrow its spatial exploration. This targeted approach can substantially decrease the number of iterations required to identify the optimal stimulation parameters, improving both the speed and accuracy of the optimization process.

## Conclusion

In this living white paper, we introduced NeuroMOSAICS, an open-access, reproducible and diverse dataset collection covering neurostimulation across different species, neural interfaces and search space dimensions. The two scenarios presented in this first version support optimization research in diverse tasks and objectives. The first dataset provides EMG responses from cortical stimulation in both awake and sedated NHPs and rats, while the second dataset focuses on bilateral EMG responses from spinal cord stimulation in sedated rats. 

This collection is an attempt to bring together open neurostimulation characterization datasets shared by the community. These datasets, often difficult to collect due to cost, ethical, and technical constraints, are typically shared only on a limited scale. By making them more widely available, we aim to support researchers in developing and validating complex optimization and data-intensive algorithms tailored to neurostimulation challenges. We aim to foster collaboration between neurostimulation researchers and the ML community, encouraging the creation of algorithms better suited to concrete neurostimulation problems.

## Data avaibility statement

The datasets presented in this living white paper are openly available on the platform OSF (https://osf.io/) :  
-	**Dataset 1** (M1 stimulations on NHPs) : https://osf.io/54vhx/, reference number : 54vhx.  
-	**Dataset 1 bis** (M1 stimulations on rats) : A similar dataset that **Dataset 1** but conducted on rats is also available at https://osf.io/54vhx/, reference number : 54vhx.
-	**Dataset 2** (spinal cord stimulations on rats) : https://osf.io/kpb7x/, reference number : kpb7x.  
Additional datasets will be progressively integrated into this living white paper. For each dataset already included, this paper is augmented: a supporting text is provided to clarify its relevance and potential applications, along with a direct link to access the data.

## Credit authorship contribution statement

**Lison Kardassevitch:** Writing – review & editing, Writing – original draft, Visualization, Project administration, Methodology, Formal analysis, Conceptualization.  
**Davide Burchielli:** Writing – review & editing.  
**Numa Dancause:** Writing – review & editing, Supervision.  
**Marco Bonizzato:** Writing – review & editing, Supervision, Resources, Project administration, Funding acquisition, Conceptualization.  

## Funding sources 

This work was supported by the Natural Sciences and Engineering Research Council of Canada (NSERC; RGPIN-2023-04370) and New Frontiers in Research Fund Exploration (NFRFE-2022-00394).

## Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Aknowledgements

The authors extend their gratitude to all scholars who have openly shared datasets for neurostimulation optimization, fostering the growth of the community. This includes the contributors who released **Dataset 1** in 2021. NeuroMOSAICS owes its existence to a steadfast community commitment to open science.


## References

```{bibliography}






