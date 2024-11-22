# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 57,
    "description": "",
    "supported_formats": [
      48,
      57
    ]
  },
  "overlays": {
    "entries": [
      {
        "formats": 48,
        "directory": "overlay_48"
      }
    ]
  }
}
```

### demo

`@loot_table demo:demo`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:stick",
          "functions": [
            {
              "function": "minecraft:set_custom_data",
              "tag": "{msg:'this remains in the normal data folder'}"
            }
          ]
        }
      ]
    }
  ]
}
```

`@loot_table demo:foo`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:stick",
          "functions": [
            {
              "function": "minecraft:set_custom_data",
              "tag": "{msg:'this is the same in both'}"
            }
          ]
        }
      ]
    }
  ]
}
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@loot_table demo:demo`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:stick",
          "functions": [
            {
              "function": "minecraft:set_custom_data",
              "tag": "{msg:'an overlay is created for this'}"
            }
          ]
        }
      ]
    }
  ]
}
```

`@endoverlay`
