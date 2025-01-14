# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 57,
    "description": "",
    "supported_formats": [
      44,
      57
    ]
  },
  "overlays": {
    "entries": [
      {
        "formats": [
          47,
          48
        ],
        "directory": "overlay_48"
      },
      {
        "formats": 47,
        "directory": "overlay_47"
      },
      {
        "formats": {
          "min_inclusive": 44,
          "max_inclusive": 44
        },
        "directory": "overlay_44"
      }
    ]
  }
}
```

### demo

`@function demo:foo`

```mcfunction
say this is the same in both
```

## Overlay `overlay_44`

`@overlay overlay_44`

### demo

`@function demo:foo`

```mcfunction
say this is in an overlay that exists already
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@function demo:demo`

```mcfunction
say this only exists in the overlay
```

## Overlay `overlay_47`

`@overlay overlay_47`

### demo

`@function demo:foo`

```mcfunction
say this is in an overlay that exists already
```

`@endoverlay`

## Resource pack

`@resource_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 57,
    "description": "",
    "supported_formats": [
      44,
      57
    ]
  },
  "overlays": {
    "entries": [
      {
        "formats": 47,
        "directory": "overlay_47"
      }
    ]
  }
}
```

### demo

`@texture demo:foo`

![texture.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAACZElEQVR4Ae1Yi2rDMAxsxv7/l7fd4MohpNrRTOQ1ChTbku70sBycHl8/z+PGz8eNc/9NvQvQHXDzCvQRuHkDPLoDugNuXoE+AjdvgH4Jfs50wHEcrhm+o6jTbyqV6RwkXFtCxVud4miX5bHcl74DoqBtUKP1Kh74meoAW3WuR4FG+r/iybuCZ6oAdPhqPLMrnm0mmRU8ywrwqjjUeUl6SdA+GlfxgH9ZATSoKKlIHiUayVfxgP/Sl2CUkBYvspmRZ3iOH1D/JzhT3Xe12eIIVBa3C1BZ/R18dwfssAuVMXQHVFZ/B9/Pq3B0vcQ9iTq9M6mMcy8hxXh6yCI8sZ7e6rhWPsg8LOOAvvwIvApQk2HQHC2Oa460G43PDmAFScD1iED1GQzxI6zqGSOxHCM59IqnPcZnAVQYzV85AEb1kcMz3Mqh3B4HbGHD0dooXnlPFcCS2rUSW1209jAabITz5B4X7SLdqQIoiRekJ1MMg9HRw6iec+WZxRCL0cOAs/wlqEHqXBNW+ep5/x+wuqL/jW/bI3BVIbsAV1V6Vz/dAbvuzFVxdQdcVeld/dy+A4bfArxD42qqc+6oJ6NOR9qpDHO98no21Hs64qmjLeSeDHL7pDqA5JYssyYXR8sRya1ddj3sgIgYgWnFIzsrV4yXXKSnnBiuLf/ZdaoAcI5AGMwZpxazKhHEYLln4kodARBnAweOP/BkggZu1ZPqADpHImcTGNmP9PTtjbopszzpDvACyMgYNEfLEcmtXXbdf4hkK/cuuPIjUF3ILkD1DlT77w6o3oFq/90B1TtQ7b87oHoHqv1/A4i35Y8io2pYAAAAAElFTkSuQmCC)

## Overlay `overlay_47`

`@overlay overlay_47`

### demo

`@texture demo:demo`

![texture.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAADkklEQVR4Ae2WiY4cMQhEM9H+/y8ny0RPKiGw8ZXpVfdIu9hAFWV8qF9/vn+/bvz7feO1v5f+NODuJ+DLGvB6vcI+2PNATJ8K9em4xxUWSepTz/NrjUyf1vF4P996BSBXAb1xhvF+P+/xVuPvE9DqdpVI8+BTX2+smGyx5te8HqfGM853AzQxG2cEUX6UOyscfsMbb8RNTmTBaUy1lBugBNlYickZFQwustFiojzvU5zXWG6AArNFZX4vKJpXsboY5Ynwqllzdbz1EVRiHbeEZLHMr7w7xq/vQs+n8I5O/lSO/3IFrtyc8iOoi4geHOJ2o4jr7VKfjg3HHA6scuHDwt3CktuyR08A4rCRkFYsylffChaeqRMAmF1gjtWdU5FZvuGyGH54mFOrhdWcbLzUAERFIkxoK+4FaS6xaLHE1K5glxrQEuhF2TzKj3weq4vV8QoWnqUGREJNlPp1HjVBcxFVtStYahx9BNkhLEUrdgYD7wj2+RKka3e1R6/AT2jqlkfQ7hwPkt6/yBc1hTwfq/BmWONSLZ6b+fYT0BJE0SvZpROQLcSaUOk+eHJpHnPiFTuDMd7tDTAhthAWUxFfyenxaXykGdsbYIuhCZWF7coZWbTWPNIAK7C7CbpA3W0WE/kUQ5632x9BX+Dq8+dL8Oo7dFrf7a/A0CPIQ6OPi/cx150jP4pZno8ztxgYfMwtxs/HmBNv2akTEImwIqN+hHkcc2yW1/MTb9mhE6BEJi7rtPr9IoyjF7ecCGd++1Xw/zL7/6caYAJMYEtkq3QPBz/Wc/XwPr81n7oCRqi70CpQiUVcka/CNZozdQIoMrtDujhOkvrgz6zmRqch8ilGeadPgJIwzopkfnCftM+X4Ce7f4XaW6/AFRY0qmHpEdRi0cNjcb3/UQ7xKKb4KA5WdYyOj58AhGO9wMyveVlO5ldsb7ztBFBIdyUSmMXxg2EOr1n1kafxmfH2BvRErAhfwWa6jl+BrPBV/NtPQG+XVo7xCjZr+PEToKIzEZ/0P1+Cn+z+FWofvwJXWGRLQ/kRbD1u3PMox8eYe1ER1nLIz+LkZHHwvh7zbScgE5D5EdCzp/HlE4DQXkc1PiO+h9c4mtRqvFJ/uAFKqsVUxMlxr77GKzqGG1AhPZkz2vRe/nADeoS9HYjiyhnFtaFRXPE6tlz7U59y2XjbI5gVyfxeSDZfxWe8+J8vQTpxV7vtCvzUBv4FVue6zIipvs8AAAAASUVORK5CYII=)

`@endoverlay`
