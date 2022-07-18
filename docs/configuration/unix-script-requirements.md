# UNIX Script Requirements

Scripts executed as OpCon jobs must meet the following requirements:

* A shell invocation line in the first line of the script.

:::tip Example

Depending on the UNIX shell in use, the invocation line may contain the following information:

```#!/bin/csh```

```#!/bin/ksh```

```#!/bin/sh```

Any other available shells may also be invoked.

:::

* If the script starts other scripts, the parent script must wait for all child scripts to finish.
* 
The script must supply an exit code. The valid Exit Code range is –127 to +127. The LSAM misinterprets any codes falling outside this range. If using STDOUT to communicate exit conditions, refer to [Redirecting STDOUT](redirecting-stdout).