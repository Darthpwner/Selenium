#!/bin/bash
cd PATH_TO_YOUR_JAR_AND_JSON_FILES
java -jar selenium-server-standalone-2.48.2.jar -role node -nodeConfig nodes.json -debug
