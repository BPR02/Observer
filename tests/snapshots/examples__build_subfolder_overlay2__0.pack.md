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

`@function demo:demo`

```mcfunction
say this remains in the normal data folder
```

`@function demo:foo`

```mcfunction
say this is the same in both
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@function demo:demo`

```mcfunction
say an overlay is created for this
```

`@endoverlay`
