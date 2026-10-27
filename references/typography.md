# Typography and exact fonts

## Establish the lettering

Preserve the user's exact text, capitalization, punctuation, line breaks, and reading direction. Resolve whether "Sapphire" names the material style, the literal word to render, or both from the request. Do not add a wordmark or title when only a material treatment was requested.

Identify the font family, weight, style, size, tracking, line spacing, and intended dimensions. Use a supplied font file or an installed font with matching internal family/style metadata. Check file metadata rather than trusting a filename. Do not silently substitute a condensed lookalike for a named typeface.

If a weight is unspecified, use a suitable installed weight and state it; a bold weight usually holds the optical treatment better at small sizes. If the requested font is unavailable, ask for an accessible font file or permission to substitute. Do not claim to have used a font that could not be loaded.

## Build the geometry reference

Use a real text renderer to typeset the exact text with the resolved font. Preserve natural aspect ratio, shaping, kerning, and counters. Render a clean high-resolution reference or obtain outlined vector letterforms where the available tools support it. Keep generous transparent padding around the lettering so highlights are not clipped.

Read and inspect the reference before styling. Keep its alpha mask or vector paths as the silhouette authority for the final composition. For DENSE, for example, load an actual Dense Regular, Dense Bold, or Dense Thin font; do not infer its letter shapes from the word "dense." DENSE is one possible input font, not a dependency or bundled font.

## Apply the material

Provide the font render as the geometry authority and the Sapphire images only as material references. Apply dark convex glass, compact blue/cyan/white caustics, restrained warm prismatic tips, and narrow chromatic aberration to the letters themselves. Preserve the exact word, letter silhouettes, counters, spacing, baseline, and line breaks.

Default to a frameless wordmark. For transparent output, require real alpha outside the letterforms and in their counters; do not add a square tile behind the word or a separate tile behind each letter. Use one consistent lighting direction across the text and maintain readability at the intended size.

Prompt recipe:

"Render the exact text [VERBATIM TEXT] using the attached real-font render as the geometry authority. Preserve every letter, counter, spacing, baseline, and line break. Apply Sapphire's dark convex optical-glass material to the letterforms themselves: compact blue/cyan/white caustics, tiny warm prismatic fringes, restrained cool/warm chromatic separation at selected edges, and quiet dark interiors. Match the style reference's optical finish without copying its icon or square tile. Transparent outside the letters and through their counters. No backdrop, enclosing plaque, extra words, ornaments, or external shadow."

## Verify fidelity and export

Compare the generated lettering with the font render character by character and at small size. Image generation can change letter geometry even when a font reference is supplied. Correct visible deviations and report any remaining uncertainty.

For a silhouette-first composition, retain the actual typeset/vector geometry as the final authority. Where the requested workflow and available tools support it, use that geometry as an editing mask or composite/clip generated optical material to the original outlines. Inspect the result rather than relying on regenerated typography. Do not present generative lettering as a mathematically exact font rendering unless the geometry was actually enforced and verified.

Retain the clean type reference and approved raster master when reproducibility is requested. Do not bundle font binaries in the skill or distribution unless the user supplied redistribution permission or the font's license explicitly permits it. Never include local machine paths in reusable prompts or distributed metadata.
