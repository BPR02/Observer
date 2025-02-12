# CHANGELOG


## v0.7.3 (2025-02-05)

### Bug Fixes

- (#2) caches now track deleted files
  ([`b303a3c`](https://github.com/BPR02/Observer/commit/b303a3cd0d8e2f396d5e9ddebb1c171d1c04c8ad))


## v0.7.2 (2025-01-16)

### Bug Fixes

- Save dp and rp overlays separately
  ([`43778ce`](https://github.com/BPR02/Observer/commit/43778ce3cae7e1486207e47cd6bb7807e5522f14))

### Chores

- Make poe commands run pyright
  ([`c83d75a`](https://github.com/BPR02/Observer/commit/c83d75a01122dbaaa64991b3b550b7cfe425a6c3))

### Code Style

- Remove double comment marker
  ([`811b8ef`](https://github.com/BPR02/Observer/commit/811b8ef114a276df9180f546046059ceab977752))

### Documentation

- Fix docstring line breaks and clarify a few comments
  ([`8f76828`](https://github.com/BPR02/Observer/commit/8f768288594bf9c1461f2e3489587b392ea5f1ec))

### Refactoring

- Remove unused parameters and functions
  ([`5a59e20`](https://github.com/BPR02/Observer/commit/5a59e20412f0fbed737d58ff0a8590849365b59b))


## v0.7.1 (2025-01-14)

### Bug Fixes

- Make nested overlays load after generated overlays
  ([`eea04a7`](https://github.com/BPR02/Observer/commit/eea04a7121e05ea4af46a153489c1d2a2f06fd0e))


## v0.7.0 (2025-01-14)

### Features

- Merge overlays from target pack
  ([`7fb09e7`](https://github.com/BPR02/Observer/commit/7fb09e74ee72e741bcbd5dc2b9dd0338eeb3bd89))


## v0.6.2 (2024-12-13)

### Bug Fixes

- Structure files don't need DataVersion to match
  ([`cb19247`](https://github.com/BPR02/Observer/commit/cb192474a41f77e9de57f398877fd46a2f3aeaa7))

### Code Style

- Run formatter
  ([`7af5549`](https://github.com/BPR02/Observer/commit/7af5549acf440cb9e46e590a68fddc7f83e3c45e))

### Documentation

- Update todo
  ([`2a59fc0`](https://github.com/BPR02/Observer/commit/2a59fc0b2dc98abbc69e2eee92694c64b5c48956))


## v0.6.1 (2024-12-13)

### Chores

- Update beet version
  ([`37e1e00`](https://github.com/BPR02/Observer/commit/37e1e00838872211eca455f51846acbc2f4f2868))

### Performance Improvements

- Introduce caching
  ([`10a085e`](https://github.com/BPR02/Observer/commit/10a085ebaf4a73c83a3caad742c1a3d27f0ae743))

### Testing

- Fix sanity test pack format
  ([`70161ec`](https://github.com/BPR02/Observer/commit/70161ec5164f724aaddc7eef3a555616aaad80bc))

- Move mcmeta deletion to tests
  ([`7f9bf67`](https://github.com/BPR02/Observer/commit/7f9bf67fbbeb5b028e00d0b733df41e95c483574))


## v0.6.0 (2024-12-11)

### Documentation

- Update todo
  ([`fdcf7e3`](https://github.com/BPR02/Observer/commit/fdcf7e30f48203e4620d0b344298ba1068a13b5b))

- Update todo
  ([`e28a209`](https://github.com/BPR02/Observer/commit/e28a20954c07a14db13f31ea99b7be9bb16fb909))

### Features

- Accept links for process location
  ([`0306a21`](https://github.com/BPR02/Observer/commit/0306a21fb221f5f5a0616c90e3db5964db4ba6f1))


## v0.5.0 (2024-12-11)

### Chores

- Delete demo_pack directory
  ([`0fb8086`](https://github.com/BPR02/Observer/commit/0fb8086b62297b500888fb5f1f4f0daf4a686870))

### Documentation

- Add poetry installation info to contributing
  ([`60aee3f`](https://github.com/BPR02/Observer/commit/60aee3fb858e980d7868518fdf1638118d0ead4e))

### Features

- Ignore overlays that exist before the plugin runs
  ([`801bb67`](https://github.com/BPR02/Observer/commit/801bb67d10e365234f213d3db4d1bf946e7c61f0))

### Testing

- Rename "nester_overlay" to "subfolder_overlay"
  ([`1d5f7eb`](https://github.com/BPR02/Observer/commit/1d5f7eb97aa8b84b8f7a98318efe975a10fb3ddc))


## v0.4.0 (2024-11-24)

### Features

- Add worldgen support ([#1](https://github.com/BPR02/Observer/pull/1),
  [`ef2ec84`](https://github.com/BPR02/Observer/commit/ef2ec848fbfd71d0aab4d2703a979573a4649c6d))

* worldgen

* don't test worldgen

- tests with worldgen files are broken in lectern snapshots:
  https://github.com/mcbeet/lectern/issues/361

* Update TODO.md


## v0.3.0 (2024-11-22)

### Features

- Generate resource pack overlays
  ([`d0855e8`](https://github.com/BPR02/Observer/commit/d0855e8dfce7a9f82edbbc641bcc7802e196f994))

- add dependency pillow


## v0.2.1 (2024-11-22)

### Bug Fixes

- Remove empty overlay entries in datapack
  ([`a3d3c96`](https://github.com/BPR02/Observer/commit/a3d3c969eda9cf485d37d81b95bafdab80c24d06))

- fixes a bug that created an empty overlay field in pack.mcmeta even if there were no overlays
  generated


## v0.2.0 (2024-11-22)

### Chores

- Fix github action release
  ([`6e0d283`](https://github.com/BPR02/Observer/commit/6e0d283250e8daeea710889e4a3b131c323d910d))

Workaround for this issue:
  https://github.com/python-semantic-release/python-semantic-release/issues/723

- Only publish on new release
  ([`f13ec64`](https://github.com/BPR02/Observer/commit/f13ec6475a7d5dda2622600b8fe839e08e455aff))

- Properly update plugin version
  ([`b1d1d6b`](https://github.com/BPR02/Observer/commit/b1d1d6b412c607ec821bc2f001395023a9464df6))

- manually update version to 0.1.0 since the github action won't do it rn

### Features

- Generate datapack overlays
  ([`c03b42c`](https://github.com/BPR02/Observer/commit/c03b42c08f2e669ccee4253d8dd0e33863d58ae9))

### Testing

- Add proper test pipeline
  ([`dd086fc`](https://github.com/BPR02/Observer/commit/dd086fc47503372a911302dad76cf8c5088367b2))


## v0.1.0 (2024-11-21)

### Features

- Setup environment
  ([`98eb502`](https://github.com/BPR02/Observer/commit/98eb50299cfc45725a89006e5cd5a74f5ce68659))

initial setup for automated build and release
