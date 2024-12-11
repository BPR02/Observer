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
      },
      {
        "formats": {
          "min_inclusive": 47,
          "max_inclusive": 47
        },
        "directory": "overlay_47"
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

## Overlay `overlay_47`

`@overlay overlay_47`

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

`@endoverlay`
