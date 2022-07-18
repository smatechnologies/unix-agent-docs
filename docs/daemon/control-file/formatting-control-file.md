# Formatting the Control File

The formatting of elements is not important to the daemon; however, SMA Technologies recommends the files be laid out for easiest readability. Carriage returns, line feeds, and non-significant spaces are optional and are ignored. Use a pound symbol (#) to "comment out" a line.

:::info Note 

Spaces in the data portion of an element are important and are considered part of the data for SMA FAD to interpret.
 
:::

:::tip Example 

The following example shows identical, valid sets of elements in a different layout:

```

<id1><elt1>a</elt1><elt2>b</elt2></id1>

- or -

<id1>
<elt1>a</elt1>
<elt2>b</elt2>
</id1>

```

:::