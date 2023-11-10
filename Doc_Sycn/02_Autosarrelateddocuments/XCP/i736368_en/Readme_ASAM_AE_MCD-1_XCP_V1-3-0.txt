/************************************************************** 
*** ASAM AE_MCD1_XCP                                        *** 
*** Version :  1.3.0                                        ***
*** Date:      2015/04/29                                   *** 
***************************************************************/

XCP 1.3. consists of one Base standard and Associated Standards 
for each physical bus or network type and the description to 
uild a Seed&Key DLL

Directory Documents: 
    Base Standard:
    - ASAM_AE_MCD-1-XCP_BS_Protocol-Layer-Specification_V1-3-0
    Transport Layer Specification:
    - ASAM_AE_MCD-1-XCP_AS_CAN-Transport-Layer_V1-3-0
    - ASAM_AE_MCD-1-XCP_AS_Ethernet-Transport-Layer_V1-3-0
    - ASAM_AE_MCD-1-XCP_AS_Flexray-Transport-Layer_V1-3-0
    - ASAM_AE_MCD-1-XCP_AS_SxI-Transport-Layer_V1-3-0
    - ASAM_AE_MCD-1-XCP_AS_USB-Transport-Layer_V1-3-0
	Seed&KeyTemplate
	- ASAM_AE_MCD-1-XCP_AS_How-to-make-a-Seed-&-Key-DLL-for-XCP_V1-0-0.docx
	
Directory AML_Sources:
    Base Standard:
    - XCPplus_v1_3.aml
    - XCP_v1_3_common.aml
    - XCP_v1_3_definitions.aml
    Transport Layer Specification:
    - XCP_v1_3_on_CAN.aml
    - XCP_v1_3_on_FLX.aml
    - XCP_v1_3_on_SxI.aml
    - XCP_v1_3_on_TCP_IP.aml
    - XCP_v1_3_on_UDP_IP.aml
    - XCP_v1_3_on_USB.aml	
	XCP_1.3_AML_example
	- XCP_v1_3_example.a2l
	- XCP_v1_3_IF_DATA_example.a2l
	- XCPplus_v1_3_IF_DATA_example.aml
	
Directory SeednKey-DLL-Template: 
    - seedNKeyXcpMain.cpp
    - Callconv.h
    - SeedNKeyXcp.dsp
    - seedNKeyXcp.h
