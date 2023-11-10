@echo off
set "SAXON_PATH=.\SaxonHE10-6J"
set "LIFM_CNF=icsp_lifm_cnf.arxml"
set "QUERY_SCRIPT=extract_lifm_cnf.xq"
set "LIFM_OUTPUT=output.xml"

java -cp "%SAXON_PATH%\saxon-he-10.6.jar" net.sf.saxon.Query -s:"%LIFM_CNF%" -q:"%QUERY_SCRIPT%" -o:"%LIFM_OUTPUT%"
