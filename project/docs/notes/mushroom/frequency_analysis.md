# Overview

This dataset is almost entirely categorical. Using them all would be maddening. Goal here, identify some obvious processing. 

## Takeaways

- `stalk_root` is the only column w/ missing values. Trash it. 
- `veil_type` is 100% "partial". Trash it.
- Multiple columns are simply booleans. Only 2 categories.
  - `poisonous` (the response)
  - `gill_attachment`
  - `gill_spacing`
  - `gill_size`
  - `stalk_shape`
- Many of the `color` columns have a ton of categories, and many with extremely low frequencies.
  - `cap_color`: 
    - cinnamon - 44 
    - purple - 16
    - green - 16
  - `cap_surface`: grooves has 4 rows
  - `gill_color`: red, yellow, orange, green all concerningly low
  - `stalk_coor_above_ring`: 
    - red - 96
    - cinnamon - 36
    - yellow - 8
  - Many other examples. Will need to examine relationship with response before thinking of solutions to avoid wasting time. 


## Copy pasted output

```
DATA STRUCTURE ---
Rows: 8123
Columns: 23

MISSING DATA - Columns with nonzero null counts ---
shape: (1, 1)
┌────────────┐
│ stalk_root │
│ ---        │
│ u32        │
╞════════════╡
│ 2480       │
└────────────┘

FREQUENCY BREAKDOWN ---

poisonous frequency ---
shape: (2, 3)
┌───────────┬──────┬────────────┐
│ poisonous ┆ freq ┆ proportion │
│ ---       ┆ ---  ┆ ---        │
│ str       ┆ u32  ┆ f64        │
╞═══════════╪══════╪════════════╡
│ edible    ┆ 4208 ┆ 0.518035   │
│ poisonous ┆ 3915 ┆ 0.481965   │
└───────────┴──────┴────────────┘

cap_shape frequency ---
shape: (6, 3)
┌───────────┬──────┬────────────┐
│ cap_shape ┆ freq ┆ proportion │
│ ---       ┆ ---  ┆ ---        │
│ str       ┆ u32  ┆ f64        │
╞═══════════╪══════╪════════════╡
│ convex    ┆ 3655 ┆ 0.449957   │
│ flat      ┆ 3152 ┆ 0.388034   │
│ knobbed   ┆ 828  ┆ 0.101933   │
│ bell      ┆ 452  ┆ 0.055644   │
│ sunken    ┆ 32   ┆ 0.003939   │
│ conical   ┆ 4    ┆ 0.000492   │
└───────────┴──────┴────────────┘

cap_surface frequency ---
shape: (4, 3)
┌─────────────┬──────┬────────────┐
│ cap_surface ┆ freq ┆ proportion │
│ ---         ┆ ---  ┆ ---        │
│ str         ┆ u32  ┆ f64        │
╞═════════════╪══════╪════════════╡
│ scaly       ┆ 3244 ┆ 0.39936    │
│ smooth      ┆ 2555 ┆ 0.314539   │
│ fibrous     ┆ 2320 ┆ 0.285609   │
│ grooves     ┆ 4    ┆ 0.000492   │
└─────────────┴──────┴────────────┘

cap_color frequency ---
shape: (10, 3)
┌───────────┬──────┬────────────┐
│ cap_color ┆ freq ┆ proportion │
│ ---       ┆ ---  ┆ ---        │
│ str       ┆ u32  ┆ f64        │
╞═══════════╪══════╪════════════╡
│ brown     ┆ 2283 ┆ 0.281054   │
│ gray      ┆ 1840 ┆ 0.226517   │
│ red       ┆ 1500 ┆ 0.184661   │
│ yellow    ┆ 1072 ┆ 0.131971   │
│ white     ┆ 1040 ┆ 0.128032   │
│ buff      ┆ 168  ┆ 0.020682   │
│ pink      ┆ 144  ┆ 0.017727   │
│ cinnamon  ┆ 44   ┆ 0.005417   │
│ purple    ┆ 16   ┆ 0.00197    │
│ green     ┆ 16   ┆ 0.00197    │
└───────────┴──────┴────────────┘

bruises frequency ---
shape: (2, 3)
┌─────────┬──────┬────────────┐
│ bruises ┆ freq ┆ proportion │
│ ---     ┆ ---  ┆ ---        │
│ str     ┆ u32  ┆ f64        │
╞═════════╪══════╪════════════╡
│ no      ┆ 4748 ┆ 0.584513   │
│ bruises ┆ 3375 ┆ 0.415487   │
└─────────┴──────┴────────────┘

odor frequency ---
shape: (9, 3)
┌──────────┬──────┬────────────┐
│ odor     ┆ freq ┆ proportion │
│ ---      ┆ ---  ┆ ---        │
│ str      ┆ u32  ┆ f64        │
╞══════════╪══════╪════════════╡
│ none     ┆ 3528 ┆ 0.434322   │
│ foul     ┆ 2160 ┆ 0.265912   │
│ fishy    ┆ 576  ┆ 0.07091    │
│ spicy    ┆ 576  ┆ 0.07091    │
│ almond   ┆ 400  ┆ 0.049243   │
│ anise    ┆ 400  ┆ 0.049243   │
│ pungent  ┆ 255  ┆ 0.031392   │
│ creosote ┆ 192  ┆ 0.023637   │
│ musty    ┆ 36   ┆ 0.004432   │
└──────────┴──────┴────────────┘

gill_attachment frequency ---
shape: (2, 3)
┌─────────────────┬──────┬────────────┐
│ gill_attachment ┆ freq ┆ proportion │
│ ---             ┆ ---  ┆ ---        │
│ str             ┆ u32  ┆ f64        │
╞═════════════════╪══════╪════════════╡
│ free            ┆ 7913 ┆ 0.974147   │
│ attached        ┆ 210  ┆ 0.025853   │
└─────────────────┴──────┴────────────┘

gill_spacing frequency ---
shape: (2, 3)
┌──────────────┬──────┬────────────┐
│ gill_spacing ┆ freq ┆ proportion │
│ ---          ┆ ---  ┆ ---        │
│ str          ┆ u32  ┆ f64        │
╞══════════════╪══════╪════════════╡
│ close        ┆ 6811 ┆ 0.838483   │
│ crowded      ┆ 1312 ┆ 0.161517   │
└──────────────┴──────┴────────────┘

gill_size frequency ---
shape: (2, 3)
┌───────────┬──────┬────────────┐
│ gill_size ┆ freq ┆ proportion │
│ ---       ┆ ---  ┆ ---        │
│ str       ┆ u32  ┆ f64        │
╞═══════════╪══════╪════════════╡
│ broad     ┆ 5612 ┆ 0.690878   │
│ narrow    ┆ 2511 ┆ 0.309122   │
└───────────┴──────┴────────────┘

gill_color frequency ---
shape: (12, 3)
┌────────────┬──────┬────────────┐
│ gill_color ┆ freq ┆ proportion │
│ ---        ┆ ---  ┆ ---        │
│ str        ┆ u32  ┆ f64        │
╞════════════╪══════╪════════════╡
│ buff       ┆ 1728 ┆ 0.212729   │
│ pink       ┆ 1492 ┆ 0.183676   │
│ white      ┆ 1202 ┆ 0.147975   │
│ brown      ┆ 1048 ┆ 0.129016   │
│ gray       ┆ 752  ┆ 0.092577   │
│ chocolate  ┆ 732  ┆ 0.090114   │
│ purple     ┆ 492  ┆ 0.060569   │
│ black      ┆ 407  ┆ 0.050105   │
│ red        ┆ 96   ┆ 0.011818   │
│ yellow     ┆ 86   ┆ 0.010587   │
│ orange     ┆ 64   ┆ 0.007879   │
│ green      ┆ 24   ┆ 0.002955   │
└────────────┴──────┴────────────┘

stalk_shape frequency ---
shape: (2, 3)
┌─────────────┬──────┬────────────┐
│ stalk_shape ┆ freq ┆ proportion │
│ ---         ┆ ---  ┆ ---        │
│ str         ┆ u32  ┆ f64        │
╞═════════════╪══════╪════════════╡
│ tapering    ┆ 4608 ┆ 0.567278   │
│ enlarging   ┆ 3515 ┆ 0.432722   │
└─────────────┴──────┴────────────┘

stalk_root frequency ---
shape: (5, 3)
┌────────────┬──────┬────────────┐
│ stalk_root ┆ freq ┆ proportion │
│ ---        ┆ ---  ┆ ---        │
│ str        ┆ u32  ┆ f64        │
╞════════════╪══════╪════════════╡
│ bulbous    ┆ 3776 ┆ 0.464853   │
│ null       ┆ 2480 ┆ 0.305306   │
│ equal      ┆ 1119 ┆ 0.137757   │
│ club       ┆ 556  ┆ 0.068448   │
│ rooted     ┆ 192  ┆ 0.023637   │
└────────────┴──────┴────────────┘

stalk_surface_above_ring frequency ---
shape: (4, 3)
┌──────────────────────────┬──────┬────────────┐
│ stalk_surface_above_ring ┆ freq ┆ proportion │
│ ---                      ┆ ---  ┆ ---        │
│ str                      ┆ u32  ┆ f64        │
╞══════════════════════════╪══════╪════════════╡
│ smooth                   ┆ 5175 ┆ 0.63708    │
│ silky                    ┆ 2372 ┆ 0.29201    │
│ fibrous                  ┆ 552  ┆ 0.067955   │
│ scaly                    ┆ 24   ┆ 0.002955   │
└──────────────────────────┴──────┴────────────┘

stalk_surface_below_ring frequency ---
shape: (4, 3)
┌──────────────────────────┬──────┬────────────┐
│ stalk_surface_below_ring ┆ freq ┆ proportion │
│ ---                      ┆ ---  ┆ ---        │
│ str                      ┆ u32  ┆ f64        │
╞══════════════════════════╪══════╪════════════╡
│ smooth                   ┆ 4935 ┆ 0.607534   │
│ silky                    ┆ 2304 ┆ 0.283639   │
│ fibrous                  ┆ 600  ┆ 0.073864   │
│ scaly                    ┆ 284  ┆ 0.034962   │
└──────────────────────────┴──────┴────────────┘

stalk_color_above_ring frequency ---
shape: (9, 3)
┌────────────────────────┬──────┬────────────┐
│ stalk_color_above_ring ┆ freq ┆ proportion │
│ ---                    ┆ ---  ┆ ---        │
│ str                    ┆ u32  ┆ f64        │
╞════════════════════════╪══════╪════════════╡
│ white                  ┆ 4463 ┆ 0.549428   │
│ pink                   ┆ 1872 ┆ 0.230457   │
│ gray                   ┆ 576  ┆ 0.07091    │
│ brown                  ┆ 448  ┆ 0.055152   │
│ buff                   ┆ 432  ┆ 0.053182   │
│ orange                 ┆ 192  ┆ 0.023637   │
│ red                    ┆ 96   ┆ 0.011818   │
│ cinnamon               ┆ 36   ┆ 0.004432   │
│ yellow                 ┆ 8    ┆ 0.000985   │
└────────────────────────┴──────┴────────────┘

stalk_color_below_ring frequency ---
shape: (9, 3)
┌────────────────────────┬──────┬────────────┐
│ stalk_color_below_ring ┆ freq ┆ proportion │
│ ---                    ┆ ---  ┆ ---        │
│ str                    ┆ u32  ┆ f64        │
╞════════════════════════╪══════╪════════════╡
│ white                  ┆ 4383 ┆ 0.539579   │
│ pink                   ┆ 1872 ┆ 0.230457   │
│ gray                   ┆ 576  ┆ 0.07091    │
│ brown                  ┆ 512  ┆ 0.063031   │
│ buff                   ┆ 432  ┆ 0.053182   │
│ orange                 ┆ 192  ┆ 0.023637   │
│ red                    ┆ 96   ┆ 0.011818   │
│ cinnamon               ┆ 36   ┆ 0.004432   │
│ yellow                 ┆ 24   ┆ 0.002955   │
└────────────────────────┴──────┴────────────┘

veil_type frequency ---
shape: (1, 3)
┌───────────┬──────┬────────────┐
│ veil_type ┆ freq ┆ proportion │
│ ---       ┆ ---  ┆ ---        │
│ str       ┆ u32  ┆ f64        │
╞═══════════╪══════╪════════════╡
│ partial   ┆ 8123 ┆ 1.0        │
└───────────┴──────┴────────────┘

veil_color frequency ---
shape: (4, 3)
┌────────────┬──────┬────────────┐
│ veil_color ┆ freq ┆ proportion │
│ ---        ┆ ---  ┆ ---        │
│ str        ┆ u32  ┆ f64        │
╞════════════╪══════╪════════════╡
│ white      ┆ 7923 ┆ 0.975379   │
│ brown      ┆ 96   ┆ 0.011818   │
│ orange     ┆ 96   ┆ 0.011818   │
│ yellow     ┆ 8    ┆ 0.000985   │
└────────────┴──────┴────────────┘

ring_number frequency ---
shape: (3, 3)
┌─────────────┬──────┬────────────┐
│ ring_number ┆ freq ┆ proportion │
│ ---         ┆ ---  ┆ ---        │
│ str         ┆ u32  ┆ f64        │
╞═════════════╪══════╪════════════╡
│ one         ┆ 7487 ┆ 0.921704   │
│ two         ┆ 600  ┆ 0.073864   │
│ none        ┆ 36   ┆ 0.004432   │
└─────────────┴──────┴────────────┘

ring_type frequency ---
shape: (5, 3)
┌────────────┬──────┬────────────┐
│ ring_type  ┆ freq ┆ proportion │
│ ---        ┆ ---  ┆ ---        │
│ str        ┆ u32  ┆ f64        │
╞════════════╪══════╪════════════╡
│ pendant    ┆ 3967 ┆ 0.488366   │
│ evanescent ┆ 2776 ┆ 0.341746   │
│ large      ┆ 1296 ┆ 0.159547   │
│ flaring    ┆ 48   ┆ 0.005909   │
│ none       ┆ 36   ┆ 0.004432   │
└────────────┴──────┴────────────┘

spore_print_color frequency ---
shape: (9, 3)
┌───────────────────┬──────┬────────────┐
│ spore_print_color ┆ freq ┆ proportion │
│ ---               ┆ ---  ┆ ---        │
│ str               ┆ u32  ┆ f64        │
╞═══════════════════╪══════╪════════════╡
│ white             ┆ 2388 ┆ 0.29398    │
│ brown             ┆ 1968 ┆ 0.242275   │
│ black             ┆ 1871 ┆ 0.230334   │
│ chocolate         ┆ 1632 ┆ 0.200911   │
│ green             ┆ 72   ┆ 0.008864   │
│ yellow            ┆ 48   ┆ 0.005909   │
│ orange            ┆ 48   ┆ 0.005909   │
│ buff              ┆ 48   ┆ 0.005909   │
│ purple            ┆ 48   ┆ 0.005909   │
└───────────────────┴──────┴────────────┘

population frequency ---
shape: (6, 3)
┌────────────┬──────┬────────────┐
│ population ┆ freq ┆ proportion │
│ ---        ┆ ---  ┆ ---        │
│ str        ┆ u32  ┆ f64        │
╞════════════╪══════╪════════════╡
│ several    ┆ 4040 ┆ 0.497353   │
│ solitary   ┆ 1712 ┆ 0.21076    │
│ scattered  ┆ 1247 ┆ 0.153515   │
│ numerous   ┆ 400  ┆ 0.049243   │
│ abundant   ┆ 384  ┆ 0.047273   │
│ clustered  ┆ 340  ┆ 0.041856   │
└────────────┴──────┴────────────┘

habitat frequency ---
shape: (7, 3)
┌─────────┬──────┬────────────┐
│ habitat ┆ freq ┆ proportion │
│ ---     ┆ ---  ┆ ---        │
│ str     ┆ u32  ┆ f64        │
╞═════════╪══════╪════════════╡
│ woods   ┆ 3148 ┆ 0.387542   │
│ grasses ┆ 2148 ┆ 0.264434   │
│ paths   ┆ 1144 ┆ 0.140835   │
│ leaves  ┆ 832  ┆ 0.102425   │
│ urban   ┆ 367  ┆ 0.04518    │
│ meadows ┆ 292  ┆ 0.035947   │
│ waste   ┆ 192  ┆ 0.023637   │
└─────────┴──────┴────────────┘
```