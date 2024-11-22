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
      },
      {
        "formats": 48,
        "directory": "overlay_48"
      }
    ]
  }
}
```

### demo

`@function demo:demo_replace`

```mcfunction
say this remains in the normal data folder
```

`@function demo:foo`

```mcfunction
say this is the same in both
```

## Overlay `default_overlay`

`@overlay default_overlay`

### demo

`@function demo:demo_delete`

```mcfunction
say this only exists in the normal data folder
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@function demo:demo_replace`

```mcfunction
say an overlay is created for this
```

`@function demo:demo_add`

```mcfunction
say this only exists in the overlay
```

`@endoverlay`
