# Deactivating LSAM Components

The UNIX LSAM has two optional components that may be deactivated. These components are sma_cronmon, and sma_filein. The methodology of deactivating a component has two basic steps:

1. Comment out the lines in ${LSAM_ROOT}/bin/start_lsam that START the component.
2. Comment out the lines in ${LSAM_ROOT}/bin/stop_lsam that STOP the component.

The following sections show the lines needing to be "commented out" to deactivate the respective component:

## Deactivating sma_cronmon

### Changes to #{LSAM_ROOT}/bin/start_lsam

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
