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
        "formats": 57,
        "directory": "default_overlay"
      }
    ]
  }
}
```

### demo

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

## Overlay `default_overlay`

`@overlay default_overlay`

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
              "tag": "{msg:'this only exists in the normal data folder'}"
            }
          ]
        }
      ]
    }
  ]
}
```

`@endoverlay`
