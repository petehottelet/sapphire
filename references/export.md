# Production export

Keep a lossless artwork master at its actual generated resolution. Preserve an input SVG or real-font geometry reference separately when requested. Do not call a raster wrapper an editable vector or imply that upscaling restores missing detail.

Honor the requested format. For transparent PNG requests, deliver RGBA PNG with a real alpha channel. Otherwise, compare optimized PNG and lossless WebP at matching resolution and choose the smaller faithful artifact appropriate to the destination. Verify alpha and visible RGB fidelity after decoding; do not assume lossy formats preserve chromatic fringes.

Preserve the requested aspect ratio. A 512px square can be a default web icon export if the source supports it; it is not a default for text, logos, banners, or illustrations. Keep typography at its natural proportions and provide enough resolution for thin counters and fine spectral edges. Never force wide artwork into a square or stretch letters to fit.

For transparent outputs, verify alpha extrema and empty areas rather than judging only the viewer background. Inspect edges on light and dark backgrounds for halos, clipping, fake checkerboards, or opaque corners. A nearly transparent antialiased edge pixel is not an opaque backdrop. Preserve intended holes and transparent padding.

For contact sheets, honor the requested background and labels. When transparency with no labels is requested, composite only the artwork onto an RGBA canvas with zero-alpha empty space. Do not add a white page, black page, checkerboard, heading, captions, or shadow behind the grid.

Use image-generation tools for creative editing. Requested deterministic encoding, resizing, typography rendering, and layout assembly are separate export/preparation steps. Use available tools and document actual outputs. If the image tool exposes no local bytes, state that measured file exports have not been produced.

When reproducibility is requested, retain the brief, exact text and resolved font metadata, accessible references, approved master, dimensions, settings, and checksums. Distinguish deterministic typesetting/encoding from stochastic image generation; do not promise bit-identical regenerated optical artwork. Keep required attribution with redistributed bundled examples and do not distribute font binaries without permission.
