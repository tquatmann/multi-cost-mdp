from collections import OrderedDict

commands = OrderedDict()
commands["single_ii_unf_dd"] = r"""
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=100,CrowdSize=20 --engine dd --statistics --timemem --logfile crowds-TotalRuns100_CrowdSize20.log
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=20,CrowdSize=20 --engine dd --statistics --timemem --logfile crowds-TotalRuns20_CrowdSize20.log
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=6,CrowdSize=20 --engine dd --statistics --timemem --logfile crowds-TotalRuns6_CrowdSize20.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=10 --engine dd --statistics --timemem --logfile nand-N60_K10.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=100 --engine dd --statistics --timemem --logfile nand-N60_K100.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=4 --engine dd --statistics --timemem --logfile nand-N60_K4.log
--prism ../cost-bounded/models/service/unfolded_care_home_scenario.prism --prop ../cost-bounded/models/service/unfolded_properties.prctl "single1" -const B1=2400 -e dd --sound -tm --logfile Service-single1-B12400.log
--prism ../cost-bounded/models/jobsched/unfolded_02procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=2,B4=130 -e dd --sound -tm --logfile JobSched2-single2-B1-1_B2-1_B32_B4130.log
--prism ../cost-bounded/models/jobsched/unfolded_03procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=3,B4=195 -e dd --sound -tm --logfile JobSched3-single2-B1-1_B2-1_B33_B4195.log
--prism ../cost-bounded/models/jobsched/unfolded_05procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=5,B4=325 -e dd --sound -tm --logfile JobSched5-single2-B1-1_B2-1_B35_B4325.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "single1" -const delay=36,B1=500,B2=10 -e dd --sound -tm --logfile FireWire-single1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "single1" -const delay=36,B1=10000,B2=10 -e dd --sound -tm --logfile FireWire-single1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "single1" -const B1=10,B2=10,B3=130 -e dd --sound -tm --logfile Resources-single1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "single1" -const B1=100,B2=100,B3=1300 -e dd --sound -tm --logfile Resources-single1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "single1" -const B1=99,B2=-1,B3=180,B4=100 -e dd --sound -tm --logfile Rover-single1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "single1" -const B1=499,B2=-1,B3=900,B4=500 -e dd --sound -tm --logfile Rover-single1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "single1" -const COUNTER=0,B1=500 -e dd --sound -tm --logfile UAV-single1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "single1" -const COUNTER=0,B1=1000 -e dd --sound -tm --logfile UAV-single1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=4000 -e dd --sound -tm --logfile Wlan3-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=10000 -e dd --sound -tm --logfile Wlan3-single1-COL0_B110000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=4000 -e dd --sound -tm --logfile Wlan6-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=10000 -e dd --sound -tm --logfile Wlan6-single1-COL0_B110000.log
""".strip().split("\n")

commands["single_ii_unf_sp"] = r"""
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=100,CrowdSize=20 --sound --native:method ii --statistics --timemem --logfile crowds-TotalRuns100_CrowdSize20.log
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=20,CrowdSize=20 --sound --native:method ii --statistics --timemem --logfile crowds-TotalRuns20_CrowdSize20.log
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=6,CrowdSize=20 --sound --native:method ii --statistics --timemem --logfile crowds-TotalRuns6_CrowdSize20.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=10 --sound --native:method ii --statistics --timemem --logfile nand-N60_K10.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=100 --sound --native:method ii --statistics --timemem --logfile nand-N60_K100.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=4 --sound --native:method ii --statistics --timemem --logfile nand-N60_K4.log
--prism ../cost-bounded/models/service/unfolded_care_home_scenario.prism --prop ../cost-bounded/models/service/unfolded_properties.prctl "single1" -const B1=2400 -e sparse --sound -tm --logfile Service-single1-B12400.log
--prism ../cost-bounded/models/jobsched/unfolded_02procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=2,B4=130 -e sparse --sound -tm --logfile JobSched2-single2-B1-1_B2-1_B32_B4130.log
--prism ../cost-bounded/models/jobsched/unfolded_03procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=3,B4=195 -e sparse --sound -tm --logfile JobSched3-single2-B1-1_B2-1_B33_B4195.log
--prism ../cost-bounded/models/jobsched/unfolded_05procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=5,B4=325 -e sparse --sound -tm --logfile JobSched5-single2-B1-1_B2-1_B35_B4325.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "single1" -const delay=36,B1=500,B2=10 -e sparse --sound -tm --logfile FireWire-single1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "single1" -const delay=36,B1=10000,B2=10 -e sparse --sound -tm --logfile FireWire-single1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "single1" -const B1=10,B2=10,B3=130 -e sparse --sound -tm --logfile Resources-single1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "single1" -const B1=100,B2=100,B3=1300 -e sparse --sound -tm --logfile Resources-single1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "single1" -const B1=99,B2=-1,B3=180,B4=100 -e sparse --sound -tm --logfile Rover-single1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "single1" -const B1=499,B2=-1,B3=900,B4=500 -e sparse --sound -tm --logfile Rover-single1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "single1" -const COUNTER=0,B1=500 -e sparse --sound -tm --logfile UAV-single1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "single1" -const COUNTER=0,B1=1000 -e sparse --sound -tm --logfile UAV-single1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=4000 -e sparse --sound -tm --logfile Wlan3-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=10000 -e sparse --sound -tm --logfile Wlan3-single1-COL0_B110000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=4000 -e sparse --sound -tm --logfile Wlan6-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=10000 -e sparse --sound -tm --logfile Wlan6-single1-COL0_B110000.log
""".strip().split("\n")

commands["single_ii_seq"] = r"""
--prism ../cost-bounded/models/crowds/crowds.prism --prop ../cost-bounded/models/crowds/crowds.props --constants TotalRuns=100,CrowdSize=20 --sound --native:method ii --statistics --timemem --logfile crowds-TotalRuns100_CrowdSize20.log
--prism ../cost-bounded/models/crowds/crowds.prism --prop ../cost-bounded/models/crowds/crowds.props --constants TotalRuns=20,CrowdSize=20 --sound --native:method ii --statistics --timemem --logfile crowds-TotalRuns20_CrowdSize20.log
--prism ../cost-bounded/models/crowds/crowds.prism --prop ../cost-bounded/models/crowds/crowds.props --constants TotalRuns=6,CrowdSize=20 --sound --native:method ii --statistics --timemem --logfile crowds-TotalRuns6_CrowdSize20.log
--prism ../cost-bounded/models/nand/nand.prism --prop ../cost-bounded/models/nand/nand.props --constants N=60,K=10 --sound --native:method ii --statistics --timemem --logfile nand-N60_K10.log
--prism ../cost-bounded/models/nand/nand.prism --prop ../cost-bounded/models/nand/nand.props --constants N=60,K=100 --sound --native:method ii --statistics --timemem --logfile nand-N60_K100.log
--prism ../cost-bounded/models/nand/nand.prism --prop ../cost-bounded/models/nand/nand.props --constants N=60,K=4 --sound --native:method ii --statistics --timemem --logfile nand-N60_K4.log
--prism ../cost-bounded/models/service/care_home_scenario.prism --prop ../cost-bounded/models/service/properties.prctl "single1" -const B1=2400 --sound -tm --logfile Service-single1-B12400.log
--prism ../cost-bounded/models/jobsched/02procs.prism --prop ../cost-bounded/models/jobsched/properties.props "single2" -const B1=-1,B2=-1,B3=2,B4=130 --sound -tm --logfile JobSched2-single2-B1-1_B2-1_B32_B4130.log
--prism ../cost-bounded/models/jobsched/03procs.prism --prop ../cost-bounded/models/jobsched/properties.props "single2" -const B1=-1,B2=-1,B3=3,B4=195 --sound -tm --logfile JobSched3-single2-B1-1_B2-1_B33_B4195.log
--prism ../cost-bounded/models/jobsched/05procs.prism --prop ../cost-bounded/models/jobsched/properties.props "single2" -const B1=-1,B2=-1,B3=5,B4=325 --sound -tm --logfile JobSched5-single2-B1-1_B2-1_B35_B4325.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "single1" -const delay=36,B1=500,B2=10 --sound -tm --logfile FireWire-single1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "single1" -const delay=36,B1=10000,B2=10 --sound -tm --logfile FireWire-single1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "single1" -const B1=10,B2=10,B3=130 --sound -tm --logfile Resources-single1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "single1" -const B1=100,B2=100,B3=1300 --sound -tm --logfile Resources-single1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "single1" -const B1=99,B2=-1,B3=180,B4=100 --sound -tm --logfile Rover-single1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "single1" -const B1=499,B2=-1,B3=900,B4=500 --sound -tm --logfile Rover-single1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "single1" -const COUNTER=0,B1=500 --sound -tm --logfile UAV-single1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "single1" -const COUNTER=0,B1=1000 --sound -tm --logfile UAV-single1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=4000 --sound -tm --logfile Wlan3-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=10000 --sound -tm --logfile Wlan3-single1-COL0_B110000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=4000 --sound -tm --logfile Wlan6-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=10000 --sound -tm --logfile Wlan6-single1-COL0_B110000.log
""".strip().split("\n")

commands["single_pi_unf_sp"] = r"""
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=100,CrowdSize=20 --exact --statistics --timemem --logfile crowds-TotalRuns100_CrowdSize20.log
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=20,CrowdSize=20 --exact --statistics --timemem --logfile crowds-TotalRuns20_CrowdSize20.log
--prism ../cost-bounded/models/crowds/unfolded_crowds.prism --prop ../cost-bounded/models/crowds/unfolded_crowds.props --constants TotalRuns=6,CrowdSize=20 --exact --statistics --timemem --logfile crowds-TotalRuns6_CrowdSize20.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=10 --exact --statistics --timemem --logfile nand-N60_K10.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=100 --exact --statistics --timemem --logfile nand-N60_K100.log
--prism ../cost-bounded/models/nand/unfolded_nand.prism --prop ../cost-bounded/models/nand/unfolded_nand.props --constants N=60,K=4 --exact --statistics --timemem --logfile nand-N60_K4.log
--prism ../cost-bounded/models/service/unfolded_care_home_scenario.prism --prop ../cost-bounded/models/service/unfolded_properties.prctl "single1" -const B1=2400 -e sparse --exact -tm --logfile Service-single1-B12400.log
--prism ../cost-bounded/models/jobsched/unfolded_02procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=2,B4=130 -e sparse --exact -tm --logfile JobSched2-single2-B1-1_B2-1_B32_B4130.log
--prism ../cost-bounded/models/jobsched/unfolded_03procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=3,B4=195 -e sparse --exact -tm --logfile JobSched3-single2-B1-1_B2-1_B33_B4195.log
--prism ../cost-bounded/models/jobsched/unfolded_05procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "single2" -const B1=-1,B2=-1,B3=5,B4=325 -e sparse --exact -tm --logfile JobSched5-single2-B1-1_B2-1_B35_B4325.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "single1" -const delay=36,B1=500,B2=10 -e sparse --exact -tm --logfile FireWire-single1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "single1" -const delay=36,B1=10000,B2=10 -e sparse --exact -tm --logfile FireWire-single1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "single1" -const B1=10,B2=10,B3=130 -e sparse --exact -tm --logfile Resources-single1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "single1" -const B1=100,B2=100,B3=1300 -e sparse --exact -tm --logfile Resources-single1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "single1" -const B1=99,B2=-1,B3=180,B4=100 -e sparse --exact -tm --logfile Rover-single1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "single1" -const B1=499,B2=-1,B3=900,B4=500 -e sparse --exact -tm --logfile Rover-single1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "single1" -const COUNTER=0,B1=500 -e sparse --exact -tm --logfile UAV-single1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "single1" -const COUNTER=0,B1=1000 -e sparse --exact -tm --logfile UAV-single1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=4000 -e sparse --exact -tm --logfile Wlan3-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=10000 -e sparse --exact -tm --logfile Wlan3-single1-COL0_B110000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=4000 -e sparse --exact -tm --logfile Wlan6-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "single1" -const COL=0,B1=10000 -e sparse --exact -tm --logfile Wlan6-single1-COL0_B110000.log
""".strip().split("\n")

commands["single_pi_seq"] = r"""
--prism ../cost-bounded/models/crowds/crowds.prism --prop ../cost-bounded/models/crowds/crowds.props --constants TotalRuns=100,CrowdSize=20 --exact --statistics --timemem --logfile crowds-TotalRuns100_CrowdSize20.log
--prism ../cost-bounded/models/crowds/crowds.prism --prop ../cost-bounded/models/crowds/crowds.props --constants TotalRuns=20,CrowdSize=20 --exact --statistics --timemem --logfile crowds-TotalRuns20_CrowdSize20.log
--prism ../cost-bounded/models/crowds/crowds.prism --prop ../cost-bounded/models/crowds/crowds.props --constants TotalRuns=6,CrowdSize=20 --exact --statistics --timemem --logfile crowds-TotalRuns6_CrowdSize20.log
--prism ../cost-bounded/models/nand/nand.prism --prop ../cost-bounded/models/nand/nand.props --constants N=60,K=10 --exact --statistics --timemem --logfile nand-N60_K10.log
--prism ../cost-bounded/models/nand/nand.prism --prop ../cost-bounded/models/nand/nand.props --constants N=60,K=100 --exact --statistics --timemem --logfile nand-N60_K100.log
--prism ../cost-bounded/models/nand/nand.prism --prop ../cost-bounded/models/nand/nand.props --constants N=60,K=4 --exact --statistics --timemem --logfile nand-N60_K4.log
--prism ../cost-bounded/models/service/care_home_scenario.prism --prop ../cost-bounded/models/service/properties.prctl "single1" -const B1=2400 --exact -tm --logfile Service-single1-B12400.log
--prism ../cost-bounded/models/jobsched/02procs.prism --prop ../cost-bounded/models/jobsched/properties.props "single2" -const B1=-1,B2=-1,B3=2,B4=130 --exact -tm --logfile JobSched2-single2-B1-1_B2-1_B32_B4130.log
--prism ../cost-bounded/models/jobsched/03procs.prism --prop ../cost-bounded/models/jobsched/properties.props "single2" -const B1=-1,B2=-1,B3=3,B4=195 --exact -tm --logfile JobSched3-single2-B1-1_B2-1_B33_B4195.log
--prism ../cost-bounded/models/jobsched/05procs.prism --prop ../cost-bounded/models/jobsched/properties.props "single2" -const B1=-1,B2=-1,B3=5,B4=325 --exact -tm --logfile JobSched5-single2-B1-1_B2-1_B35_B4325.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "single1" -const delay=36,B1=500,B2=10 --exact -tm --logfile FireWire-single1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "single1" -const delay=36,B1=10000,B2=10 --exact -tm --logfile FireWire-single1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "single1" -const B1=10,B2=10,B3=130 --exact -tm --logfile Resources-single1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "single1" -const B1=100,B2=100,B3=1300 --exact -tm --logfile Resources-single1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "single1" -const B1=99,B2=-1,B3=180,B4=100 --exact -tm --logfile Rover-single1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "single1" -const B1=499,B2=-1,B3=900,B4=500 --exact -tm --logfile Rover-single1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "single1" -const COUNTER=0,B1=500 --exact -tm --logfile UAV-single1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "single1" -const COUNTER=0,B1=1000 --exact -tm --logfile UAV-single1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=4000 --exact -tm --logfile Wlan3-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=10000 --exact -tm --logfile Wlan3-single1-COL0_B110000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=4000 --exact -tm --logfile Wlan6-single1-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "single1" -const COL=0,B1=10000 --exact -tm --logfile Wlan6-single1-COL0_B110000.log
""".strip().split("\n")

commands["multi_ii_unf_sp"] = r"""
--prism ../cost-bounded/models/service/unfolded_care_home_scenario.prism --prop ../cost-bounded/models/service/unfolded_properties.prctl "multi1" -const B1=2400 -e sparse --sound -tm --logfile Service-multi1-B12400.log
--prism ../cost-bounded/models/jobsched/unfolded_02procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "multi1" -const B1=2,B2=65,B3=2,B4=130 -e sparse --sound -tm --logfile JobSched2-multi1-B12_B265_B32_B4130.log
--prism ../cost-bounded/models/jobsched/unfolded_03procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "multi1" -const B1=2,B2=65,B3=3,B4=195 -e sparse --sound -tm --logfile JobSched3-multi1-B12_B265_B33_B4195.log
--prism ../cost-bounded/models/jobsched/unfolded_05procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "multi1" -const B1=2,B2=65,B3=5,B4=325 -e sparse --sound -tm --logfile JobSched5-multi1-B12_B265_B35_B4325.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "multi1" -const delay=36,B1=500,B2=10 -e sparse --sound -tm --logfile FireWire-multi1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "multi1" -const delay=36,B1=10000,B2=10 -e sparse --sound -tm --logfile FireWire-multi1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "multi1" -const B1=10,B2=10,B3=130 -e sparse --sound -tm --logfile Resources-multi1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "multi1" -const B1=100,B2=100,B3=1300 -e sparse --sound -tm --logfile Resources-multi1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "multi1" -const B1=99,B2=-1,B3=180,B4=100 -e sparse --sound -tm --logfile Rover-multi1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "multi1" -const B1=499,B2=-1,B3=900,B4=500 -e sparse --sound -tm --logfile Rover-multi1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "multi1" -const COUNTER=0,B1=500 -e sparse --sound -tm --logfile UAV-multi1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "multi1" -const COUNTER=0,B1=1000 -e sparse --sound -tm --logfile UAV-multi1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=4000 -e sparse --sound -tm --logfile Wlan3-multi3-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=10000 -e sparse --sound -tm --logfile Wlan3-multi3-COL0_B110000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=4000 -e sparse --sound -tm --logfile Wlan6-multi3-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=10000 -e sparse --sound -tm --logfile Wlan6-multi3-COL0_B110000.log
""".strip().split("\n")

commands["multi_ii_seq"] = r"""
--prism ../cost-bounded/models/service/care_home_scenario.prism --prop ../cost-bounded/models/service/properties.prctl "multi1" -const B1=2400 --sound -tm --logfile Service-multi1-B12400.log
--prism ../cost-bounded/models/jobsched/02procs.prism --prop ../cost-bounded/models/jobsched/properties.props "multi1" -const B1=2,B2=65,B3=2,B4=130 --sound -tm --logfile JobSched2-multi1-B12_B265_B32_B4130.log
--prism ../cost-bounded/models/jobsched/03procs.prism --prop ../cost-bounded/models/jobsched/properties.props "multi1" -const B1=2,B2=65,B3=3,B4=195 --sound -tm --logfile JobSched3-multi1-B12_B265_B33_B4195.log
--prism ../cost-bounded/models/jobsched/05procs.prism --prop ../cost-bounded/models/jobsched/properties.props "multi1" -const B1=2,B2=65,B3=5,B4=325 --sound -tm --logfile JobSched5-multi1-B12_B265_B35_B4325.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "multi1" -const delay=36,B1=500,B2=10 --sound -tm --logfile FireWire-multi1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "multi1" -const delay=36,B1=10000,B2=10 --sound -tm --logfile FireWire-multi1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "multi1" -const B1=10,B2=10,B3=130 --sound -tm --logfile Resources-multi1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "multi1" -const B1=100,B2=100,B3=1300 --sound -tm --logfile Resources-multi1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "multi1" -const B1=99,B2=-1,B3=180,B4=100 --sound -tm --logfile Rover-multi1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "multi1" -const B1=499,B2=-1,B3=900,B4=500 --sound -tm --logfile Rover-multi1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "multi1" -const COUNTER=0,B1=500 --sound -tm --logfile UAV-multi1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "multi1" -const COUNTER=0,B1=1000 --sound -tm --logfile UAV-multi1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=4000 --sound -tm --logfile Wlan3-multi3-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=10000 --sound -tm --logfile Wlan3-multi3-COL0_B110000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=4000 --sound -tm --logfile Wlan6-multi3-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=10000 --sound -tm --logfile Wlan6-multi3-COL0_B110000.log
""".strip().split("\n")

commands["multi_pi_unf"] = r"""
--prism ../cost-bounded/models/service/unfolded_care_home_scenario.prism --prop ../cost-bounded/models/service/unfolded_properties.prctl "multi1" -const B1=2400 -e sparse --exact -tm --logfile Service-multi1-B12400.log
--prism ../cost-bounded/models/jobsched/unfolded_02procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "multi1" -const B1=2,B2=65,B3=2,B4=130 -e sparse --exact -tm --logfile JobSched2-multi1-B12_B265_B32_B4130.log
--prism ../cost-bounded/models/jobsched/unfolded_03procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "multi1" -const B1=2,B2=65,B3=3,B4=195 -e sparse --exact -tm --logfile JobSched3-multi1-B12_B265_B33_B4195.log
--prism ../cost-bounded/models/jobsched/unfolded_05procs.prism --prop ../cost-bounded/models/jobsched/unfolded_properties.props "multi1" -const B1=2,B2=65,B3=5,B4=325 -e sparse --exact -tm --logfile JobSched5-multi1-B12_B265_B35_B4325.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "multi1" -const delay=36,B1=500,B2=10 -e sparse --exact -tm --logfile FireWire-multi1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/unfolded_firewire_abst.prism --prop ../cost-bounded/models/firewire/unfolded_properties.props "multi1" -const delay=36,B1=10000,B2=10 -e sparse --exact -tm --logfile FireWire-multi1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "multi1" -const B1=10,B2=10,B3=130 -e sparse --exact -tm --logfile Resources-multi1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/unfolded_resources5_5.prism --prop ../cost-bounded/models/resources/unfolded_properties.prctl "multi1" -const B1=100,B2=100,B3=1300 -e sparse --exact -tm --logfile Resources-multi1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "multi1" -const B1=99,B2=-1,B3=180,B4=100 -e sparse --exact -tm --logfile Rover-multi1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/unfolded_rover.prism --prop ../cost-bounded/models/rover/unfolded_properties.props "multi1" -const B1=499,B2=-1,B3=900,B4=500 -e sparse --exact -tm --logfile Rover-multi1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "multi1" -const COUNTER=0,B1=500 -e sparse --exact -tm --logfile UAV-multi1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/unfolded_uav.prism --prop ../cost-bounded/models/uav/unfolded_properties.props "multi1" -const COUNTER=0,B1=1000 -e sparse --exact -tm --logfile UAV-multi1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=4000 -e sparse --exact -tm --logfile Wlan3-multi3-COL0_B14000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan3.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=10000 -e sparse --exact -tm --logfile Wlan3-multi3-COL0_B110000.log
--prism ../cost-bounded/models/wlan/unfolded_wlan6.nm --prop ../cost-bounded/models/wlan/unfolded_properties.prctl "multi3" -const COL=0,B1=4000 -e sparse --exact -tm --logfile Wlan6-multi3-COL0_B14000.log
""".strip().split("\n")

commands["multi_pi_seq"] = r"""
--prism ../cost-bounded/models/service/care_home_scenario.prism --prop ../cost-bounded/models/service/properties.prctl "multi1" -const B1=2400 --exact -tm --logfile Service-multi1-B12400.log
--prism ../cost-bounded/models/jobsched/02procs.prism --prop ../cost-bounded/models/jobsched/properties.props "multi1" -const B1=2,B2=65,B3=2,B4=130 --exact -tm --logfile JobSched2-multi1-B12_B265_B32_B4130.log
--prism ../cost-bounded/models/jobsched/03procs.prism --prop ../cost-bounded/models/jobsched/properties.props "multi1" -const B1=2,B2=65,B3=3,B4=195 --exact -tm --logfile JobSched3-multi1-B12_B265_B33_B4195.log
--prism ../cost-bounded/models/jobsched/05procs.prism --prop ../cost-bounded/models/jobsched/properties.props "multi1" -const B1=2,B2=65,B3=5,B4=325 --exact -tm --logfile JobSched5-multi1-B12_B265_B35_B4325.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "multi1" -const delay=36,B1=500,B2=10 --exact -tm --logfile FireWire-multi1-delay36_B1500_B210.log
--prism ../cost-bounded/models/firewire/firewire_abst.prism --prop ../cost-bounded/models/firewire/properties.props "multi1" -const delay=36,B1=10000,B2=10 --exact -tm --logfile FireWire-multi1-delay36_B110000_B210.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "multi1" -const B1=10,B2=10,B3=130 --exact -tm --logfile Resources-multi1-B110_B210_B3130.log
--prism ../cost-bounded/models/resources/resources5_5.prism --prop ../cost-bounded/models/resources/properties.prctl "multi1" -const B1=100,B2=100,B3=1300 --exact -tm --logfile Resources-multi1-B1100_B2100_B31300.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "multi1" -const B1=99,B2=-1,B3=180,B4=100 --exact -tm --logfile Rover-multi1-B199_B2-1_B3180_B4100.log
--prism ../cost-bounded/models/rover/rover.prism --prop ../cost-bounded/models/rover/properties.props "multi1" -const B1=499,B2=-1,B3=900,B4=500 --exact -tm --logfile Rover-multi1-B1499_B2-1_B3900_B4500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "multi1" -const COUNTER=0,B1=500 --exact -tm --logfile UAV-multi1-COUNTER0_B1500.log
--prism ../cost-bounded/models/uav/uav.prism --prop ../cost-bounded/models/uav/properties.props "multi1" -const COUNTER=0,B1=1000 --exact -tm --logfile UAV-multi1-COUNTER0_B11000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=4000 --exact -tm --logfile Wlan3-multi3-COL0_B14000.log
--prism ../cost-bounded/models/wlan/wlan3.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=10000 --exact -tm --logfile Wlan3-multi3-COL0_B110000.log
--prism ../cost-bounded/models/wlan/wlan6.nm --prop ../cost-bounded/models/wlan/properties.prctl "multi3" -const COL=0,B1=4000 --exact -tm --logfile Wlan6-multi3-COL0_B14000.log
""".strip().split("\n")

commands["quantiles_ii"] = r"""
""".strip().split("\n")

commands["quantiles_pi"] = r"""
""".strip().split("\n")



