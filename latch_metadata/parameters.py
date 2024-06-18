
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input': NextflowParameter(
        type=LatchFile,
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'chr': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Main options',
        description='Only use reads mapping to a specific chromosome/region. Has to be specified as in bam: i.e chr1, chr{1..22} (gets all reads mapping to chr1 to 22), 1, "X Y", incorrect naming will lead to a potentially silent error.',
    ),
    'no_read_QC': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If specified, no quality control will be performed on extracted reads. Useful, if this is done anyways in the subsequent workflow.',
    ),
    'no_stats': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If specified, skips all quality control and stats computation, including `FastQC` on both input bam and output reads, `samtools flagstat`, `samtools idxstats`, and `samtools stats`.',
    ),
    'reads_in_memory': NextflowParameter(
        type=typing.Optional[int],
        default=100000,
        section_title=None,
        description="Reads to store in memory [default = '100000']. Only relevant for use with `--samtools_collate_fast`.",
    ),
    'samtools_collate_fast': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Uses fast mode for samtools collate in `sortExtractMapped`, `sortExtractUnmapped` and `sortExtractSingleEnd`.',
    ),
    'genome': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Reference genome options',
        description='Name of iGenomes reference.',
    ),
    'fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to FASTA genome file.',
    ),
    'fasta_fai': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to FASTA FAI genome index file.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

