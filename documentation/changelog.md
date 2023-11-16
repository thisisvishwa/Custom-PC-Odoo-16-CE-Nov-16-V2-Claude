# Changelog

## [Unreleased]

### Added
- Initial setup of the Custom PC Building module.
- Models for product components, build configurations, and compatibility rules.
- Customized product views for component selection.
- Custom PC configuration wizard with step-by-step component selection, real-time compatibility checking, budget tracking, and recommendations based on use case.
- Report for bill of materials.
- Customized sales order and invoice to link to configuration.
- Scheduled actions to check for component availability.
- Overridden procurement and reordering rules for components.
- Dedicated custom PC production process with build tasks assignment, quality control checks, and assembly services management.
- User guide with documentation of custom PC configuration process, recommended component selections for common use cases, budgeting guide and tips, and assembly services details.
- Developer guide with overview of module architecture and key components, explanation of compatibility rules, instructions for adding new components, configuring recommendations, testing matrix, and versioning and migration strategy.
- Security measures including customer account requirement for saving configurations, encrypted storage of configuration data, CSRF protection on forms, input sanitization and output encoding, and access control on backend customization options.
- SEO optimizations for product component pages, unique meta titles and descriptions for each component, and structured data for rich snippets.
- Performance improvements including lazy loading for component images, caching of compatibility rules, debouncing rapid configuration changes, asynchronous stock checking, and minification of JS/CSS assets.
- Analytics tracking for popular configurations and component conversion rates, and recommendations dashboard based on metrics.
- Testing setup with unit tests using Python's unittest, Selenium browser testing, staging environment mirroring production, and load testing with Locust.
- Documentation including end user support site/forum, detailed installation guide, this changelog, and translation contributions through Launchpad.

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [0.0.1] - 2022-01-01
- Initial project setup.