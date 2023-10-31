# tsnkit

A simple scheduling toolkit for Time-Sensitive Network in Python.

```
@article{xue2023real,
  title={Real-Time Scheduling for Time-Sensitive Networking: A Systematic Review and Experimental Study},
  author={Xue, Chuanyu and Zhang, Tianyu and Zhou, Yuanbin and Han, Song},
  journal={arXiv preprint arXiv:2305.16772},
  year={2023}
}
```



## Install

Install from source:

```
git clone https://github.com/ChuanyuXue/tsnkit
cd tsnkit
python setup.py install
```


Or install from pip:

`pip install -U tsnkit `



## Usage

**Testing**

`python3 -m tsnkit.models.[METHOD] [STREAM PATH] [NETWORK PATH]`

**Reproduce the benchmark paper results:**

1. Check out to `legacy` branch.
2. Download `data.gz` from git-lfs, and unzip it to `data` folder.
3. Go `src` foder and run `python main.py --method=ALL --start=0 --end=38400`.

*Both `main` and `legacy` branches use the same logic (models & algorithms). We have enhanced the organization of the `main` branch by introducing a common interface and standardized type notation, aiming to improve maintainability and ease of extension. The `legacy` branch contains the source code used in the paper.*



## Supported methods:

| Method   | Paper                                                        |
| -------- | ------------------------------------------------------------ |
| SMT-WA   | [Scheduling Real-Time Communication in IEEE 802.1Qbv Time Sensitive Networks](https://dl.acm.org/doi/pdf/10.1145/2997465.2997470) |
| AT       | [IEEE 802.1Qbv Gate Control List Synthesis Using Array Theory Encoding](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8430062) |
| JRS-WA   | [ILP-based joint routing and scheduling for time-triggered networks](https://dl.acm.org/doi/pdf/10.1145/3139258.3139289?casa_token=RfXCSV_16bgAAAAA:ErHwYiCRp7DrH3JiSQX6_kOtmb62FqrfWiS4HeirDZvLog3tq9aiyc_GYcRnezpAOE8WBICdT25u) |
| JRS-NW   | [How to Optimize Joint Routing and Scheduling Models for TSN Using Integer Linear Programming](https://www2.informatik.uni-stuttgart.de/bibliothek/ftp/ncstrl.ustuttgart_fi/INPROC-2021-01/INPROC-2021-01.pdf) |
| JRS-NW-L | [Exploring Practical Limitations of Joint Routing and Scheduling for TSN with ILP](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8607243&casa_token=ynpoxBcgvFgAAAAA:na1WepOT9xvsfq_ZhUGKTakW6Uq65ZkAFG-tGVl3B5ZKVg1xEzXgYv2yfxjiHC-c2cW6qfE8) |
| JRS-MC   | [ILP-Based Routing and Scheduling of Multicast Realtime Traffic in Time-Sensitive Networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9203662&casa_token=vuhKuWFB-5sAAAAA:FBdBVQgf5PP7otfBJ6zFZZ9kknGJ2xZkNpl1ipBAhk3MUUin2kKJOjD3JMAha6EZ6XgnsX7c) |
| SMT-NW   | [No-wait Packet Scheduling for IEEE Time-sensitive Networks (TSN)](https://dl.acm.org/doi/pdf/10.1145/2997465.2997494?casa_token=Aly_nknYS_4AAAAA:vfTQkiQpQoQFHIq83fHcBLOlwpZ-u64UtvcDIeL65iHPneYsufwslgMbk2I8JPV4R14rKAz38JrWYg) |
| LS-TB    | [Large-scale periodic scheduling in time-sensitive networks](https://reader.elsevier.com/reader/sd/pii/S0305054821002549?token=7B7B66E61DB026B7D82D9C2B43832904B7D8FE90493FDCD741B060FEA19F6A47EF7FA8666D97C19DD2D76BCBA03B27D3&originRegion=us-east-1&originCreation=20220425171034) |
| LS       | [Heuristic List Scheduler for Time Triggered Traffic in Time Sensitive Networks](https://dl.acm.org/doi/pdf/10.1145/3314206.3314208) |
| SMT-FR   | [Joint Algorithm of Message Fragmentation and No-Wait Scheduling for Time-Sensitive Networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9317715) |
| I-ILP    | [Routing and Scheduling of Time-Triggered Traffic in Time-Sensitive Networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8889667&casa_token=6YrBm7jYR74AAAAA:3uXBqhABDDmDRtLWytsDbxtl2iKRjJDsYvFaMflMALJndY4lNTZngVbV2znSSq9heY5eh00LQw) |
| CP-WA    | [Constraint programming approaches to joint routing and scheduling in time-sensitive networks](https://pdf.sciencedirectassets.com/271420/1-s2.0-S0360835221X00058/1-s2.0-S0360835221002217/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJGMEQCIDqpmiVnioUsRYP0WQGfVWDATuxt5x0Rer85S9m0xYSKAiBHv0D1%2FALjqBg13t60tjpzBXyZjEgcqF8GgoAP83CYjyrVBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIM2pajvw4OrTdJaeB4KqkEwOY7laXnronDNsx2z6lm7pJ3SICxlkkh92oZi%2ByEvbP6RFILq73ifDlJxIAOkz2NpOwl89weiC8%2BT8hJnz3pA49S6WBPQzBP728%2BQoAywM5jT93txyGljMnq7vz0KnnGJwgRY10H2be4VJIZvTHJhS0l3OGqG5usM4iKmyGrysrLKOvLRMw8nZAT37D5CC3XDVBwtr65JvgREvH1NF6VGUDHReRNcesY1YkqPc%2FefPbn1aY8nbb%2FvhrIHohXqn%2FGBgPuvrZeYB3hdcR%2FQdPxHQa1L0UcmCBcjyjNr%2F%2FEgU4OPTqWCUbt28F1t13dBYI2JzvGnpqXEzMV7v%2FgfYAb9pORgflAPXuznb%2Fj0un5hcPrJLdtZxAuHj36FagZ0yP%2Bv%2BEU7kMzhOHw7GQxuLJKbguNO6d1H5T9%2FYGTzRMldKbPIiywTlj4frYrKkSWHd4mxUoXwdCIxkOPYbzS%2B2ZUi1sI2plkCTnffecyMkjRaSaV6Zmy00DWLzfWDB1xM%2F%2BMF2HixqDerrrsYTlmU%2BGWn2Ml7mXIKS6NHbT5pG9LU3Kb4BfGRivnId90NdFcxpgzDCHJur6STZJ51UvEoCGzvNUpe73WXyleF45r7Zton8vD23O5j23OOjFe3oecRxmIqVvv13shAcpq7oPgk%2FnCpJ9f1Ue%2BjYIt7mbhyHhwwD1%2F8mPucelJFglaIl4R7u%2Bbpc5i6NQHiriVo%2BOvm6xLA6axUkcsffiVvDDuloqZBjqqAZUw5ycZjhv1OpncoZHVSdaYQYC7Tiww4eEY5eWmYWbBOgcMUFNgO%2FkYAtA04oJMtkt9ESVdxfBzw%2FU0loVVOHF18qr65ThcSMXSGzfWBbUbwXZ4svjysKPXczlzCzVs3BfvFmxK2w%2FS8%2BEyvj9VYMpiwrQTORyaepSsPnaE4vvGDKN7W0mNDvuzXUzEVy3qXW%2F3HWpLtsVMpzsV3KMgPsHPMCUH40BufW4X&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220915T031100Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYZSZPPQSZ%2F20220915%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=dbd283d80fa4c01dd5c202fae0e9dbd7b58918296d71334523d8d40f347aa063&hash=175888141457622ec39a59c34d720806b226c1f3fbad99c907cb4f5aa117c71d&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0360835221002217&tid=spdf-52529842-e538-4517-935d-86a0e1799eb0&sid=2b6bac3e33d6f9466c4833b-505152db370egxrqa&type=client&ua=52530504510550595401&rr=74ae2c292c955a57) |
| I-OMT    | [Real-Time Scheduling of Massive Data in Time Sensitive Networks With a Limited Number of Schedule Entries](https://ieeexplore.ieee.org/document/8951090) |
| SMT-PR   | [Time-Triggered Scheduling for Time-Sensitive Networking with Preemption](https://ieeexplore.ieee.org/document/9712545) |
| CG       | [Time-Triggered Trafﬁc Planning for Data Networks with Conﬂict Graphs](https://ieeexplore.ieee.org/document/9113114) |
| DT       | [Efficient Flow Scheduling for Industrial Time-Sensitive Networking: A Divisibility Theory-Based Method](https://ieeexplore.ieee.org/document/9714183) |
| LS-PL    | [HERMES: Heuristic Multi-queue Scheduler for TSN Time-Triggered Traffic with Zero Reception Jitter Capabilities](https://dl.acm.org/doi/abs/10.1145/3534879.3534906) |



## IO format

All algorithm input and output are defined in `csv` format.

### Input:

**Stream set format:**

| id  | src | dst     | size | period | deadline | jitter |
| --- | --- | ------- | ---- | ------ | -------- | ------ |
| 0   | 0   | [7,8,9] | 50   | 100000 | 44600    | 0      |

- **id:** Unique ID for each flow
- **src:** Talker that the end-system where flow starts at.
- **dst:** Listener that the the end-system where flow ends at, formatted as list for multicast
- **size:** Packet size of each flow in Bytes.
- **period:** Flow periods in Nanoseconds.
- **deadline:** Relative flow deadline requirement in Nanoseconds.
- **jitter:** Maximum end-to-end delay variance requirement in Nanoseconds.

**Network for mat:**

| link   | q_num | rate | t_proc | t_prop |
| ------ | ----- | ---- | ------ | ------ |
| (0, 1) | 8     | 1    | 1000   | 0      |

- **link:** Directional link connects two devices.
- **q_num:** Number of available queues for time-triggered (critical) traffic.
- **rate:** Bandwidth of link in <u>bit / nanosecond</u>, e.g., 1 = 1 Gbps, 0.1 = 100 Mbps, 0.01 = 10 Mbps.
- **t_proc:** Processing time including switching fabric and ingress processing.
- **t_prop:** Propogation delay on wire after transmission.

### Output

**GCL:**

| link   | queue | start | end  | cycle    |
| ------ | ----- | ----- | ---- | -------- |
| (0, 1) | 0     | 1000  | 5000 | 12000000 |

- **queue:** Indicator implies which queue is open between start and end time.
- **start:** Relative time when queue opens in hyper period.
- **end:** Relative time when queue opens in hyper period.
- **cycle:** Cycle time of GCL.

**Offset:**

| stream | frame | offset |
| ------ | ----- | ------ |
| 0      | 0     | 1000   |

- **stream:** Unique ID for each stream.
- **frame:** The index of corresponding flow instance
- **offset:** The traffic dispatching time on end-system for corresponding flow instance

**Route:**

| stream | link  |
| ------ | ----- |
| 0      | (8,1) |
| 0      | (1,2) |
| 0      | (2,3) |

- **link:** Directional link connects two devices.

**Queueing assignment:**

| id  | frame | link  | queue |
| --- | ----- | ----- | ----- |
| 0   | 0     | (8,1) | 2     |

- **link:** Directional link connects two devices.
- **queue:** The egress queue for corresponding flow instance on corresponding link.




## Contribute

Please feel free to add your own scheduling algorithm! Refer `src/tsnkit/models/__init__.py` to impliment the required interface and benchmark entrance.
