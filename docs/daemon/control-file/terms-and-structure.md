# Terms and Structure

Familiarization with the following terms is helpful in creating Control Files:

* Element: A Control File component consisting of a start tag, data, and an end tag.
    * Start Tag: The first component of an element. The format is the less than character (<), the element name, and the greater than character (>). For example: ```<element>```.
    * Element Data: The second component of an element. This is the data that is entered in the OpCon database. In some cases, the data is optional.
    * End Tag: The last component of an element. The format is the less than character (<), a slash character (/), the element name, and the greater than character (>). For example: ```</element>```.

:::tip Example

The following example shows a single complete element:

```

<mypay>

$1000

</mypay>

``` 

The element name is **mypay** and the data associated with the element is **$1000**.

:::

* Nesting: The placement of one element inside another. A parent element requires one or more child elements placed in its data.
    * Parent Element: An element requiring one or more nested elements in its data.
    * Child Element: An element placed within the data of another element. If a child element is not placed within the parent element, the data is invalid.

:::info Note

Some elements can be both parent and child elements.

:::

:::tip Example

The following example shows nested elements in a parent/child relationship:

```

<jobdef>

<schedname>Schedule1</schedname>

<jobname>Job1</jobname>

</jobdef>

``` 

The **schedname** and **jobname** child elements are nested in the **jobdef** parent element.

:::