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

`@dimension demo:foo`

```json
{
  "type": "demo:this-is-the-same-in-both",
  "generator": {
    "type": "minecraft:debug"
  }
}
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@dimension demo:demo`

```json
{
  "type": "demo:this-only-exists-in-the-overlay",
  "generator": {
    "type": "minecraft:debug"
  }
}
```

`@endoverlay`
