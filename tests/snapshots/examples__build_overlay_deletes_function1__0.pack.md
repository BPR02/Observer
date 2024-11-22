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

`@function demo:foo`

```mcfunction
say this is the same in both
```

## Overlay `default_overlay`

`@overlay default_overlay`

### demo

`@function demo:demo`

```mcfunction
say this only exists in the normal data folder
```

`@endoverlay`
