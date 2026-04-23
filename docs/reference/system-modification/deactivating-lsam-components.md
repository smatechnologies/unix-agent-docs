---
title: Deactivating Agent Components
description: "Steps to deactivate the optional sma_cronmon and sma_filein components of the Unix Agent by commenting out lines in the start and stop scripts."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Deactivating agent components

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Steps to deactivate the optional sma_cronmon and sma_filein components of the Unix Agent by commenting out lines in the start and stop scripts.

The Unix Agent has two optional components that you can deactivate. These components are sma_cronmon, and sma_filein. The methodology of deactivating a component has two basic steps:

- You are reducing the agent's resource footprint by disabling optional components that are not required in your environment.

To deactivate a component, complete the following steps:

1. Comment out the lines in ${LSAM_ROOT}/bin/start_lsam that START the component.
2. Comment out the lines in ${LSAM_ROOT}/bin/stop_lsam that STOP the component.

The component is deactivated and will no longer start or stop with the agent.

The following sections show the lines needing to be "commented out" to deactivate the respective component:

## Deactivating sma_cronmon

### Changes to ${LSAM_ROOT}/bin/start_lsam

To comment out a line, precede it with a pound (#) symbol.

```

#!/bin/sh

 
# START_IT="yes"

# if [ -f ${CRON_PID} ]

# then

# ${LSAM_ROOT}/bin/check_process -p`cat ${CRON_PID}`

# if [ $? -eq 0 ]

# then

# echo "--- CronMon is already running."

#

# START_IT="no"

# else

# echo "--- Removing invalid pid file : ${CRON_PID}"

# rm ${CRON_PID}

# fi

# fi

# if [ ${START_IT} = "yes" ]

# then

# ${ECHO} "- Starting CronMon : ${ENDER}"

# ${LSAM_ROOT}/bin/sma_cronmon -v

# ${LSAM_ROOT}/bin/sma_cronmon

# fi

# sleep 1

#

```

### Changes to ${LSAM_ROOT}/bin/stop_lsam

To comment out a line, precede it with a pound (#) symbol.

```

#!/bin/sh

 
# ${ECHO} "- Stopping the CronMon : ${ENDER}"

# if [ -f ${CRON_PID} ]

# then

# kill -USR1 `cat ${CRON_PID}`

# echo "-- [ success ]"

# else

# echo "-- [ failed ]"

# echo " - CronMon is not running"

# fi

# sleep 1

#

```

## Deactivating sam_filein

### Changes to ${LSAM_ROOT}/bin/start_lsam

To comment out a line, precede it with a pound (#) symbol.

```

#!/bin/sh

 
# START_IT="yes"

# if [ -f ${FLIN_PID} ]

# then

# ${LSAM_ROOT}/bin/check_process -p`cat ${FLIN_PID}`

# if [ $? -eq 0 ]

# then

# echo "--- Filein is already running."

# START_IT="no"

# else

# echo "--- Removing invalid pid file : ${FLIN_PID}"

# rm ${FLIN_PID}

# fi

# fi

# if [ ${START_IT} = "yes" ]

# then

# ${ECHO} "- Starting Filein : ${ENDER}"

# ${LSAM_ROOT}/bin/sma_filein -v

# ${LSAM_ROOT}/bin/sma_filein

# fi

# sleep 1

#

```

### Changes to ${LSAM_ROOT}/bin/stop_lsam

To comment out a line, precede it with a pound (#) symbol.

```

#!/bin/sh

 
# ${ECHO} "- Stopping the Filein : ${ENDER}"

# if [ -f ${FLIN_PID} ]

# then

# kill -USR1 `cat ${FLIN_PID}`

# echo "-- [ success ]"

# else

# echo "-- [ failed ]"

# echo " - Filein is not running"

# fi

# sleep 1

```

## Exception handling

**After restarting the agent, sma_cronmon or sma_filein still appears in the status output.**
The lines in `${LSAM_ROOT}/bin/start_lsam` were not commented out correctly, or the file was not saved before the agent was restarted. Reopen `start_lsam`, confirm that every line in the relevant component block is preceded by a `#` symbol, save the file, stop the agent, and start it again.

**The stop script reports `[ failed ]` and `CronMon is not running` or `Filein is not running` when the agent is stopped.**
The component's PID file (`${CRON_PID}` or `${FLIN_PID}`) was not found, which means the component was already stopped or never started. If the component has been deactivated in `start_lsam`, also comment out the corresponding lines in `${LSAM_ROOT}/bin/stop_lsam` so the stop script no longer attempts to send a signal to a process that is not running.
