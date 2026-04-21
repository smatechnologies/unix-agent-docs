---
sidebar_label: 'sma_job_step'
title: sma_job_step
description: "Reference for the sma_job_step utility, which logs named job steps to the SAM to enable job restart at a specific step from the OpCon Enterprise Manager."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_job_step

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for the sma_job_step utility, which logs named job steps to the SAM to enable job restart at a specific step from the OpCon Enterprise Manager.

## When would you use it?

- A job consists of multiple named steps and, after a failure, you need to restart the job from a specific step rather than rerunning all preceding steps.
- You need to run only a subset of a job's steps by specifying a starting step (`sma_first`) and/or an ending step (`sma_last`) in the Job Details screen.

## Why would you use it?

- Logging steps with sma_job_step populates the Job Restart Step list in the Enterprise Manager, giving operators a named list of steps to choose from when restarting a failed job.
- Defining start and end steps avoids reprocessing data that was already successfully handled in earlier steps, reducing runtime and preventing duplicate processing.

The sma_job_step utility instructs the agent to send a message to the SAM to log a job step for later use in restarting the job.

## Syntax

```$SMA_BINDIR/sma_job_step <step_number> <step_label>```

```<step_number>```, which must be an integer greater than or equal to 1, is a sequence number to be associated with ```<step_label>```. In the TJS, its value comes from Shell variable "step_number". If two calls within the same job to "sma_job_step" use the same ```<step_number>```, the latter ```<step_label>``` will overwrite the former. 

The Enterprise Manager does not display the step number along with the label, nor is the step number supplied to the agent in restarting a job; therefore, each step label encountered should only be sent once, or the Enterprise Manager and OpCon database will be needlessly cluttered.

```<step_label>``` is the label of the step to be logged; in the SMA Technologies-supplied Template Job Script (TJS) the value comes from Shell variable "current_step".

:::tip Example

The following example shows a script using the sma_job_step utility to send step label "weekly_prd", number 3.

```
. . .

$SMA_BINDIR/sma_job_step 3 weekly_prd

. . .
```

:::

## Specifying "start step" and "end step" from job details

In order to specify a starting and/or ending step for a job using the sma_job_step utility, one or two parameters need to be appended with an intervening space to the "Start Image" or pre-pended with an intervening space to the "Parameters" in the OpCon Job Details as follows:

[ sma_first=start_step ] [ sma_last=end_step ]

start_step and end_step are Step Labels as defined in the preceding section, e.g., "abc" or "weekly_1".

Step Labels can be anything up to sixty (60) characters long that is supported for case labels by the UNIX shell scripting language. However, SMA Technologies recommends that Step Labels be confined to letters, digits, and the underscore ('_'). 

Letter case is significant (i.e., "ghi" and 'GHI' are not the same label). The first character of a Step Label must be a letter.

:::warning

'sma_first', 'sma_last', and 'sma_undefined' are step labels with special meaning and must not be used by you. Use of these labels by you may result in erratic behavior, including, but not limited to, creation of infinite loops or issuance of erroneous error messages.

:::

Both step-indicator parameters are optional, and they may be specified in either order. They must come before any of the job's other start parameters, which is why SMA Technologies recommends that they be appended to the job's start image in the "Start Image". 

If a starting step is not specified, then the job will be started at the beginning (except as may be overridden by you invoking the Job Restart Step function from Enterprise Manager Operation). 

If an ending step is not specified, the job will run clear to the end. 

If both are defined and identical, then the single step will run (unless a Job Restart Step has been specified, in which case execution will commence at that step).

:::tip Example

Step-indicator parameters (assume no Job Restart Step):

```sma_first=def sma_last=ghi``` (run steps 'def' thru 'ghi')

```sma_first=weekly_1 ```(run from step 'weekly_1' to end-of-job)

```sma_last=prod_step_xyz``` (run from beginning-of-job thru step 'prod_step_xyz')

```sma_first=s9 sma_last=s9``` (run only step 's9')


Inclusion of step-indicator parameters in the "Start Image" would resemble:

```/usr/john/jobs/some_job sma_first=start_here sma_last=stop_here```

Inclusion of step-indicatior parameters in the "Parameters" would resemble:

```sma_first=start_here sma_last=stop_here p1 xyz [[JOB_NAME]]```

Inclusion of step-indicator parameters in both the "Start Image" and Parameters":

```/usr/john/jobs/some_job sma_first=start_here``` (Start Image)

```sma_last=stop_here p1 xyz [[JOB_NAME]]``` (Parameters)

This is confusing, and SMA Technologies recommends that this practice be avoided.

:::

:::info Note

SMA Technologies recommends that [both] step-indicator parameters be appended to the job's start image in the "Start Image" within the OpCon Job Details.

:::

## Job script requirements

In order to make use of either the Job Restart Step or the Job Start/End Step capability, users' top level job scripts will need to meet certain requirements as set forth here. SMA Technologies includes a Template Job Script (TJS) with the LSAM distribution. It is reproduced below and edited to make a complete job script (edits shown in **bold** text beginning about half way down the script):

---

>```current_step="sma_undefined"```
>
>```last_step="sma_undefined"```
>
>```got_first_step="N"```
>
>```got_restart_step="N"```
>
>```while [ 1 ]```
>
>```do```
>
>```step=`expr "$1" : "sma_first=\(.*\)"` ```
>
>```if [ $? -eq 0 ]```
>
>```then```
>
>```if [ "$got_first_step" = "N" ]```
>
>```then```
>
>```if [ "$current_step" = "sma_undefined" ]```
>
>``then``
>
>```current_step="$step"```
>
>```fi```
>
>```got_first_step="Y"```
>
>```shift 1```
>
>```continue```
>
>```else```
>
>```echo "[sma_lsam] STARTING_STEP multiply-defined (539)"```
>
>```echo ""sma_lsam] STARTING_STEP multiply-defined (539)" 1>&2```
>
>```$SMA_BINDIR/sma_LSAM_feedback "[sma_lsam] STARTING_STEP multiply-defined (539)"```
>
>```$SMA_BINDIR/sma_job_step 1 "*****END*****"```
>
>```exit 1```
>
>```fi```
>
>```fi```
>
>```step=`expr "$1" : "sma_last=\(.*\)"` ```
>
>```if [ $? -eq 0 ]```
>
>```then```
>
>```if [ "$last_step" = "sma_undefined" ]```
>
>```then```
>
>```last_step="$step"```
>
>```shift 1```
>
>```continue```
>
>```else```
>
>```echo "[sma_lsam] ENDING_STEP multiply-defined (540)"```
>
>```echo "[sma_lsam] ENDING_STEP multiply-defined (540)" 1>&2```
>
>```$SMA_BINDIR/sma_LSAM_feedback "[sma_lsam] ENDING_STEP multiply-defined (540)"```
>
>```$SMA_BINDIR/sma_job_step 1 "*****END*****"```
>
>```exit 1```
>
>```fi```
>
>```fi```
>
>```step=`expr "$1" : "sma_restart=\(.*\)"` ```
>
>```if [ $? -eq 0 ]```
>
> ```then```
>
>```if [ "$got_restart_step" = "N" ]```
> 
>```then```
>
> ```current_step="$step"```
>
>```got_restart_step="Y"```
>
>```shift 1```
>
>```continue```
>
>```else```
>
>```echo "[sma_lsam] RESTART_STEP multiply-defined (541)"```
>
>```echo "[sma_lsam] RESTART_STEP multiply-defined (541)" 1>&2```
>
>```$SMA_BINDIR/sma_LSAM_feedback "[sma_lsam] RESTART_STEP multiply-defined (541)"```
>
>```$SMA_BINDIR/sma_job_step 1 "*****END*****"```
>
>```exit 1```
>
>```fi```
>
>```fi```
>
>```break```
>
>```done```
>
>```if [ "$last_step" = "sma_undefined" ]```
>
>```then```
>
>```last_step="sma_last"```
>
>```fi```
>
>```if [ "$current_step" = "sma_undefined" ]```
>
>```then```
>
>```current_step="sma_first"```
>
>```fi```
>
>```##########################```
>
>```##### Place user code common to all steps here.```
>
>```echo Execute from [$current_step] to [$last_step]```
>
>```##########################```
>
>```number_of_steps=4 ##### User is to set value.```
>
>```step_number=1```
>
>```step_list=""```
>
>```while [ 1 ]```
>
>```do```
>
>```step_found=`expr "$step_list" : ".* $current_step "` ```
>
>```if [ $step_found -eq 0 ]```
>
>```then```
>
>```$SMA_BINDIR/sma_job_step $step_number $current_step```
>
>```step_list="$step_list $current_step "```
>
>```fi```
>
>```case $current_step in```
>
>```##########################```
>
>```##### Start per-step user code after 'sma_first | '```
>
>```sma_first |``` **abc )** 
>
>**echo abc**
>
> ```next_step="def"```
>
>```;;```
>
>```def )```
>
>```echo def```
>
>```next_step="ghi"```
>
>```;;```
>
>```ghi)```
>
>```echo ghi```
>
>```next_step="jkl"```
>
>```;;```
>
>```jkl )```
>
>```echo jkl```
>
>```##### End User Code```
>
>```##########################```
>
>```next_step="sma_last"```
>
>```;;```
>
>```sma_last )```
>
>```echo sma_last```
>
>```;;```
>
>```* )```
>
>```echo "[sma_lsam] Invalid job step [$current_step] (508)"```
>
>```echo "[sma_lsam] Invalid job step [$current_step] (508)" 1>&2```
>
>```$SMA_BINDIR/sma_LSAM_feedback "[sma_lsam] Invalid job step [$current_step] (508)"```
>
>```step_number=`expr $step_number + 1` ```
>
>```$SMA_BINDIR/sma_job_step $step_number "*****END*****"```
>
>```exit 1```
>
>```;;```
> 
>```esac```
>
>```step_number=`expr $step_number + 1` ```
>
>```if [ "$current_step" == "$last_step" ]```
>
>```then```
>
>```$SMA_BINDIR/sma_job_step $step_number "*****END*****"```
> 
>```exit 0```
>
>```else```
>
>```current_step="$next_step"```
>
>```fi```
>
>```if [ $step_number -gt $number_of_steps ]```
>
>```then```
>
>```echo "[sma_lsam] Infinite loop detected (509)"```
>
>```echo "[sma_lsam] Infinite loop detected (509)" 1>&2```
>
>```$SMA_BINDIR/sma_LSAM_feedback "[sma_lsam] Infinite loop detected (509)"```
>
>```$SMA_BINDIR/sma_job_step $step_number "*****END*****"```
>
>```exit 1```
>
>```fi```
>
>```done```

---

The script exits (i.e., the job terminates) with a code of 1 if an error is detected in Job Step formatting or processing. These exit codes may be changed as desired.

Let's first take a look at the section of the TJS from "Start per-step user code..." to "End User Code". This is where users will put "the meat" of the job – everything that the job needs to accomplish. 

With the exception of the preceding two sections of the script, none the rest of the TJS should be edited in any way, as its purpose is to set-up and manage Job Steps.

:::warning

Editing any other portion of the template job script, besides as explained here, may result in erratic behavior, including but not limited to, creation of infinite loops or issuance of erroneous error messages.

:::

The example edited TJS contains four (4) job steps. All steps have some common features, while the first and the last steps have some unique features. The important parts of each step, at least so far as this part of the discussion is concerned, are the first line and the last two lines. 

The first line provides the label for the step, and the last two lines specify the next step to be run and terminate the step.

Step Labels can be anything that is supported for case labels by the UNIX shell scripting language, and up to sixty (60) characters long; however, SMA Technologies recommends that Step Labels be confined to letters, digits, and the underscore ('_'). 

Letter case is significant, i.e., "ghi" and 'GHI' are not the same label. The first character of a Step Label must be a letter. The edited TJS has four user-defined steps: 'abc', 'def', 'ghi', and 'jkl'.

:::info Note

The very first job step ('abc'), does not appear by itself like the others, but is preceded by the text "sma_first". 'sma_first', 'sma_last', and 'sma_undefined' are Step Labels with special meaning and must not be used by you. If you does not specify a starting step in the Job Details (explained later), or has not defined a Job Restart step, then the first step to run will be the one labeled 'sma_first' – which just happens to be the same step as the first user-defined step.

:::

:::warning

 'sma_first', 'sma_last', and 'sma_undefined' are Step Labels with special meaning and must not be used by you. Use of these labels by you may result in erratic behavior, including, but not limited to, creation of infinite loops or issuance of erroneous error messages.

:::

The next to the last line of each step (except for the last step) must be ``` 'next_step="___" ' ```, where the "___" is replaced with the name of the next step to run. The double quotes (" ") are required. The next step to run need not be the next step which physically follows in the script, as will be made clearer in just a moment.


Keep in mind that letter case is significant in defining Step Labels, and ensure that the 'next_step' references some step within the script, or the job will be terminated with an "[sma_lsam] Infinite loop detected (509)" message.


Excepting for the final [user-defined] step ('jkl'), the last line of a job step is a line containing two semi-colons (';;'). There can be no spaces in-between. This serves to mark the end of the step and to begin running the step indicated by 'next_step'.

:::info Note

Remember that the first user-defined step and the last user-defined step are formatted slightly differently than other user-defined steps.

:::

Execution of steps normally flows from top-to-bottom. From the initial step in the script to run, steps will run one-by-one until the final step to run. No steps will be skipped or repeated.

However, as mentioned a couple of paragraphs back, it is possible to run steps out-of-order and to repeat steps. This is accomplished by setting 'next_step' within the "actual work" of a step (i.e., 'next_step' can be set from anywhere in the step's logic and not just in the next to the last line). The "actual work" of each of the steps in the edited TJS are the 'echo' commands. The step management logic is a UNIX Shell 'case' command nested within a 'while' command.

Any Shell command that is legal inside a 'while'/'case' combination can be used, including the 'if' command. It is possible to make a decision at execution time as to what the next step to run will be by setting Shell variable 'next_step' as appropriate. As long as it is a defined Step Label (within the enclosing 'case' command), it can be any label – further down in the script, earlier in the script, or even pointing to itself, so that the current step will be immediately repeated.

It is possible to set up sophisticated processing with the edited TJS. For example, step 'def' could well be:

```

def )

echo "def -- My Variable = $my_variable"

if [ my_variable –eq 1 ]

then

next_step="ghi"

elif [ my_variable –eq 2 ]

then

next_step="abc"

elif [ my_variable –eq 3 ]

then

next_step="def"

else

next_step="jkl"

fi

my_variable=`expr "$my_variable + 1"`

;;

```

The above snippet of code has not been tested and is not guaranteed to be syntactically correct. It is provided for discussion purposes only. Note that 'next_step' need not be given a value in the next to the last line within a step. It just has to be set somewhere in the step's logic to avoid the "[sma_lsam] Infinite loop detected (509)" message mentioned above.

If 'next_step' were to refer to a non-existent step, the enclosing 'while'/'case' command logic would never end. This is clearly unacceptable. This situation is prevented from occurring by Shell variables 'number_of_steps' and 'step_number'. Notice that just a little above step "sma_first | abc" in the TJS that 'number_of_steps' gets set to 4. Also notice the comment "User is to set value." With every step that gets run, 'step_number' gets incremented. If it becomes equal to 'number_of_steps', the job is terminated with the "[sma_lsam] Infinite loop detected (509)" message.

Figuring out what value to give 'number_of_steps' is easy if there is no logic included in the script to alter the logic flow of single-stepping from top to bottom. The value required is simply the number of steps which have been defined, which in our edit TJS is 4. However, if complex job logic flow is included, then a best-guess determination of the number of steps actually to run must be made. If guessing too little, the job may be [seemingly abnormally] terminated with the "[sma_lsam] Infinite loop detected (509)" message.

On the other hand, if the 'number_of_steps' are set too high, and 'next_step' happens to get set to some non-existent step or gets set to repeatedly [but, not necessarily immediately] return control to the same step, then CPU time will be wasted in detecting the error and issuing the "[sma_lsam] Infinite loop detected (509)" message. So, make the best guess as to the number of steps to actually run, but err on the side of too many.

:::info Note

Do not forget to set 'number_of_steps'.

:::

And, finally in our discussion of the TJS, notice the line which reads:

```$SMA_BINDIR/sma_job_step $step_number $current_step```

This command serves to inform the SAM which step is about to run, so the SAM can populate the list which is presented to you when the Job Restart Step capability is invoked from the Enterprise Manager. Because steps may be repeatedly run, the script makes sure that only the first execution gets noted to the SAM to avoid unnecessary clutter in the Enterprise Manager and the OpCon database. This is done because the SAM does not provide the agent with the step number upon job restart. It only provides the step label defined from the Enterprise Manager. So, writers of job scripts need to understand that it is not possible for the SAM or the agent to determine the path taken to the Restart Step during the previous run of the job if the step may be reached via multiple paths.

Also notice the logging of step ``` "*****END*****" ``` near the bottom of the TJS. This serves to mark in the Enterprise Manager the end of the list of steps run during "this" run of the job. If a previous run of the job had resulted in more [distinct] steps getting run than in "this" execution, they would continue to be visible in the Enterprise Manager after the first end marker encountered while reading the list from top-to-bottom. For example, if the edited TJS were run from start to finish, the list of job steps displayed in the Enterprise Manager would be:

```
sma_first

def

ghi

jkl

sma_last

*****END*****

```
 
The display shows that the entire job ran (from pseudo steps "sma_first" to "sma_last"). This also shows that you specified neither a "Start Step" nor an "End Step", since both SMA Technologies-supplied pseudo-steps ran and step "abc" (which is the same step as "sma_first") is missing from the list. After restarting the job from step "jkl", the list would be:

```

jkl

sma_last

*****END*****

jkl

sma_last

*****END*****

``` 

By noting the position of the end marker in the display after the job had been restarted, one can see that only two steps ran, "jkl" and "sma_last".

If step "def" had been modified to repeat itself (until the job was terminated due to detection of an infinite loop), only one instance of step "def" would appear in the list. If you had specified a Start Step twice so that error message number 539 were issued, then no steps would have run and the end marker would appear at the top of the list of steps displayed in the Enterprise Manager. 

The list is not cleared if Job Details are edited (such as changing "Start Image" to add/modify Start/End Steps) and the job restarted. In order for the list to be cleared, the job and/or schedule must be deleted and re-built. 

There is a need for an end marker so the list of steps run, during the most recent execution of a job, could be easily ascertained.

By inspecting the first half of the TJS, up to three parameters are removed (via the 'shift' commands) from the list of start parameters passed to the job. The order of these three parameters is not dictated. One of them (if included) will indicate the step at which the job is to be restarted, while the other two (if included) will indicate the starting and/or ending steps.

The agent will supply the restart step parameter ("sma_restart=...") when you invokes the Job Restart Step function, and the parameters for starting and ending steps ("sma_first=..." and "sma_last=...") are provided by you as outlined in the following section. Because of the location and use of the 'shift' commands, users may easily adapt existing job scripts into the TJS. 

There is no need to alter the start parameters expected by the original script (i.e., $1 in the original script will remain $1 in the adapted script).

:::info Note

Users are not required to make use of the SMA Technologies-supplied template job script. At present, only start parameter "sma_restart=..." is supplied to a job by the agent, and you is free to develop any Start/End Step logic, whether in script or compiled program. However, if the concept of Start Step and End Step are at some future date included in OpCon's Central Components (and thus in the Enterprise Manager), then the agent will also supply start parameters "sma_first=..." and "sma_last=...". If you develops some other logic, then the job may cease to function properly if the agent is later upgraded.

:::
