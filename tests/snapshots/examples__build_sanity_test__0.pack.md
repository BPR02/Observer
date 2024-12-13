# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 57,
    "description": ""
  },
  "overlays": {
    "entries": [
      {
        "formats": {
          "min_inclusive": 48,
          "max_inclusive": 48
        },
        "directory": "overlay_48"
      }
    ]
  }
}
```

### demo

`@function demo:demo`

```mcfunction
say I'm here now
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@function demo:demo`

```mcfunction
say I was here first
```

`@endoverlay`
