# Lectern snapshot

## Resource pack

`@resource_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 42,
    "description": "",
    "supported_formats": [
      34,
      42
    ]
  },
  "overlays": {
    "entries": [
      {
        "formats": 34,
        "directory": "overlay_34"
      }
    ]
  }
}
```

### demo

`@texture demo:demo`

![texture.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAACI0lEQVR4nO1a0XLEIAi8dPr/v2yf0nEYDSwsklb37U4lBBE2m1yttfbZGF/VDlTjBKDagWpsH4BvprHruob/t9Z+x/qa2/8nx59sMfHKDJjdfAaoGSB3L7pbKzo0NQAWILs7mssOyvIAWDC6yaxjsTwAoyIosbIGvLIIzpBRE67zLLA5HmuARkaezqqF/MxsjNqp15ZcI+HKALRI3fPlOk8RZBdOUxfQKreljGjZYpnXz5ldEy1ppgBoTvXjIwfuFO5TGbE/soVkwlNQXDxAGrREndlsRoH0kifXEZApGKWs6BG41/RzvTXg37dBbSMOEap2oBquIogSlNFaCUQ1mq33gJYBK5/gmKBrgtpOMFQjZtmiBUAjKAiixAsBXRNccRRemQE3GEHQiBFTK9y+DR4iVO1ANbYPgFoEWbKWNs6QzTwwZwAqRSG9vP/NkM0QQG3QKkVpbcpzUx7NwAJzAKJMT1vHlM0QQEWQLWtl2rcCZoLeHdJkNct1n67lZYfhNsiSp6twmGC1A9XYPgDhx2HLC0kGU5zZjiItA2bMTo5bbHjWWkGVxG4gTNDC6bNY4Oez8BuhiOOZMtspgixDKBNEkHkE0jLgr/CrwwSrHajG9gEwa4IjMDQ71qd4s/UawhmQxdZWrYckMeu4x/noN0fe65sDwHwj64F2/dQPJd8ANOjW+bQjgL4HkDaj672a42s1wVXH7DDBageqcQJQ7UA1fgCpdoTeLV21QgAAAABJRU5ErkJggg==)

`@texture demo:foo`

![texture.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAACZElEQVR4Ae1Yi2rDMAxsxv7/l7fd4MohpNrRTOQ1ChTbku70sBycHl8/z+PGz8eNc/9NvQvQHXDzCvQRuHkDPLoDugNuXoE+AjdvgH4Jfs50wHEcrhm+o6jTbyqV6RwkXFtCxVud4miX5bHcl74DoqBtUKP1Kh74meoAW3WuR4FG+r/iybuCZ6oAdPhqPLMrnm0mmRU8ywrwqjjUeUl6SdA+GlfxgH9ZATSoKKlIHiUayVfxgP/Sl2CUkBYvspmRZ3iOH1D/JzhT3Xe12eIIVBa3C1BZ/R18dwfssAuVMXQHVFZ/B9/Pq3B0vcQ9iTq9M6mMcy8hxXh6yCI8sZ7e6rhWPsg8LOOAvvwIvApQk2HQHC2Oa460G43PDmAFScD1iED1GQzxI6zqGSOxHCM59IqnPcZnAVQYzV85AEb1kcMz3Mqh3B4HbGHD0dooXnlPFcCS2rUSW1209jAabITz5B4X7SLdqQIoiRekJ1MMg9HRw6iec+WZxRCL0cOAs/wlqEHqXBNW+ep5/x+wuqL/jW/bI3BVIbsAV1V6Vz/dAbvuzFVxdQdcVeld/dy+A4bfArxD42qqc+6oJ6NOR9qpDHO98no21Hs64qmjLeSeDHL7pDqA5JYssyYXR8sRya1ddj3sgIgYgWnFIzsrV4yXXKSnnBiuLf/ZdaoAcI5AGMwZpxazKhHEYLln4kodARBnAweOP/BkggZu1ZPqADpHImcTGNmP9PTtjbopszzpDvACyMgYNEfLEcmtXXbdf4hkK/cuuPIjUF3ILkD1DlT77w6o3oFq/90B1TtQ7b87oHoHqv1/A4i35Y8io2pYAAAAAElFTkSuQmCC)

## Overlay `overlay_34`

`@overlay overlay_34`

### demo

`@texture demo:demo`

![texture.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAB7ElEQVR4nO2byW4EIQxEIcr//7JzIkIMBttgihF+Ui69uKvNVng6mYgoPcwPWgCaSABaAJpf7wfknD+OlWmnnKunod4xT1x7QO/le8e5605wZAgQ0f8fByoJ7kMgpfnLEVHKOUOScM0kiLIj1wyBct1prukBKHJY4ceJBKAFoGF9wIqFHa3no/Oj+Cv6RvG6PUBqYXcjjb9T39AJ9lq4HC/OrW7RNsOadd8ifna/JKarFW6TNjq/Gr+mN8y4xjBPgpLxJXWAbcwd1LFGcYc9wKOFOGH1kLLeb6HbA7iMcWP8m81kWGG0ADSRALQANM8n4EhNsMB59JaT8zKsByBL4TVHe0AP9CoMT8DM7XkDS4DH5sgCLAG3zAHXLYOn54TYC6AFoIkEoAWgUZXFU9KVtbXXSCzyasm9RVUWn4Eoa0vhYovL4rPzFkc3KrvXx7iC64q2wpIRmrWYZ1l8FlvKVieo/WFk57OsqMvit5S1Z7Gl8VRl8W+Ge6ewwmgBaCIBaAFonk/AxzLo6eNHSPz/7JMciwZ1D7D6+FMlMO1zWCO0cx8gEaX5QEqC9H7RdtgixqPFNTGlm7NjVeFTfku76TIPAcn/ANTXtvsEC5Jhpe156klQ+vnMbcRegOF5IxQJQAtAEwlAC0DzfAL+AJkqWYfL672uAAAAAElFTkSuQmCC)

`@endoverlay`
