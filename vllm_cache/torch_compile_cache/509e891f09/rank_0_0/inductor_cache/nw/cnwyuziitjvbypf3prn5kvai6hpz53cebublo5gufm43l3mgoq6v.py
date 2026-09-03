# AOT ID: ['1_inference']
from ctypes import c_void_p, c_long, c_int
import torch
import math
import random
import os
import tempfile
from math import inf, nan
from cmath import nanj
from torch._inductor.hooks import run_intermediate_hooks
from torch._inductor.utils import maybe_profile
from torch._inductor.codegen.memory_planning import _align as align
from torch import device, empty_strided
from torch._inductor.async_compile import AsyncCompile
from torch._inductor.select_algorithm import extern_kernels
import triton
import triton.language as tl
from torch._inductor.runtime.triton_heuristics import start_graph, end_graph
from torch._C import _cuda_getCurrentRawStream as get_raw_stream
from torch._C import _cuda_getCurrentRawStream as get_raw_stream

aten = torch.ops.aten
inductor_ops = torch.ops.inductor
_quantized = torch.ops._quantized
assert_size_stride = torch._C._dynamo.guards.assert_size_stride
assert_alignment = torch._C._dynamo.guards.assert_alignment
empty_strided_cpu = torch._C._dynamo.guards._empty_strided_cpu
empty_strided_cuda = torch._C._dynamo.guards._empty_strided_cuda
empty_strided_xpu = torch._C._dynamo.guards._empty_strided_xpu
reinterpret_tensor = torch._C._dynamo.guards._reinterpret_tensor
alloc_from_pool = torch.ops.inductor._alloc_from_pool
async_compile = AsyncCompile()
empty_strided_p2p = torch._C._distributed_c10d._SymmetricMemory.empty_strided_p2p


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/ic/cicrwesre7aujijgwyxre5mwztiipgthdh56vr65zozdnij4ypwb.py
# Topologically Sorted Source Nodes: [to, to_1, add, pow_1, mean, add_1, rsqrt, mul, to_3, mul_1], Original ATen: [aten._to_copy, aten.add, aten.pow, aten.mean, aten.rsqrt, aten.mul]
# Source node to ATen node mapping:
#   add => add_12
#   add_1 => add_25
#   mean => mean
#   mul => mul_17
#   mul_1 => mul_22
#   pow_1 => pow_1
#   rsqrt => rsqrt
#   to => convert_element_type_2
#   to_1 => convert_element_type_3
#   to_3 => convert_element_type_5
# Graph fragment:
#   %convert_element_type_2 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mm, torch.float32), kwargs = {})
#   %convert_element_type_3 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%arg3_1, torch.float32), kwargs = {})
#   %add_12 : [num_users=3] = call_function[target=torch.ops.aten.add.Tensor](args = (%convert_element_type_2, %convert_element_type_3), kwargs = {})
#   %pow_1 : [num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%add_12, 2), kwargs = {})
#   %mean : [num_users=1] = call_function[target=torch.ops.aten.mean.dim](args = (%pow_1, [-1], True), kwargs = {})
#   %add_25 : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%mean, 1e-05), kwargs = {})
#   %rsqrt : [num_users=1] = call_function[target=torch.ops.aten.rsqrt.default](args = (%add_25,), kwargs = {})
#   %mul_17 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%add_12, %rsqrt), kwargs = {})
#   %convert_element_type_5 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mul_17, torch.bfloat16), kwargs = {})
#   %mul_22 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%convert_element_type_5, %arg4_1), kwargs = {})
triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_0 = async_compile.triton('triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_0', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 8192, 'r0_': 8192},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*bf16', 'in_ptr2': '*bf16', 'out_ptr1': '*bf16', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (5,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 5, 'num_reduction': 1, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False}
)
@triton.jit
def triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_0(in_ptr0, in_ptr1, in_ptr2, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    r0_numel = 5120
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    x0 = xindex
    _tmp7 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp0 = tl.load(in_ptr0 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp2 = tl.load(in_ptr1 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp1 = tmp0.to(tl.float32)
        tmp3 = tmp2.to(tl.float32)
        tmp4 = tmp1 + tmp3
        tmp5 = tmp4 * tmp4
        tmp6 = tl.broadcast_to(tmp5, [XBLOCK, R0_BLOCK])
        tmp8 = _tmp7 + tmp6
        _tmp7 = tl.where(r0_mask & xmask, tmp8, _tmp7)
    tmp7 = tl.sum(_tmp7, 1)[:, None]
    for r0_offset in range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp9 = tl.load(in_ptr0 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp11 = tl.load(in_ptr1 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp21 = tl.load(in_ptr2 + (r0_1), r0_mask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp10 = tmp9.to(tl.float32)
        tmp12 = tmp11.to(tl.float32)
        tmp13 = tmp10 + tmp12
        tmp14 = 5120.0
        tmp15 = (tmp7 / tmp14)
        tmp16 = 1e-05
        tmp17 = tmp15 + tmp16
        tmp18 = libdevice.rsqrt(tmp17)
        tmp19 = tmp13 * tmp18
        tmp20 = tmp19.to(tl.float32)
        tmp22 = tmp20 * tmp21
        tl.store(out_ptr1 + (r0_1 + 5120*x0), tmp22, r0_mask & xmask)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/ho/cho65ducevd25qr7rjdf4dsvys34kcxnrghj2mcldl3ojnlla4bn.py
# Topologically Sorted Source Nodes: [silu, mul_2], Original ATen: [aten.silu, aten.mul]
# Source node to ATen node mapping:
#   mul_2 => mul_34
#   silu => convert_element_type_8, convert_element_type_9, mul_29, sigmoid
# Graph fragment:
#   %convert_element_type_8 : [num_users=2] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%slice_1, torch.float32), kwargs = {})
#   %sigmoid : [num_users=1] = call_function[target=torch.ops.aten.sigmoid.default](args = (%convert_element_type_8,), kwargs = {})
#   %mul_29 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%convert_element_type_8, %sigmoid), kwargs = {})
#   %convert_element_type_9 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mul_29, torch.bfloat16), kwargs = {})
#   %mul_34 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%convert_element_type_9, %slice_2), kwargs = {})
triton_poi_fused_mul_silu_1 = async_compile.triton('triton_poi_fused_mul_silu_1', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 134217728}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_mul_silu_1', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 2, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_mul_silu_1(in_ptr0, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x0 = (xindex % 14336)
    x1 = xindex // 14336
    x2 = xindex
    tmp0 = tl.load(in_ptr0 + (x0 + 28672*x1), xmask).to(tl.float32)
    tmp5 = tl.load(in_ptr0 + (14336 + x0 + 28672*x1), xmask).to(tl.float32)
    tmp1 = tmp0.to(tl.float32)
    tmp2 = tl.sigmoid(tmp1)
    tmp3 = tmp1 * tmp2
    tmp4 = tmp3.to(tl.float32)
    tmp6 = tmp4 * tmp5
    tl.store(out_ptr0 + (x2), tmp6, xmask)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/zn/czneqnhsli2emo23ulpdo3rgccsv2emebzipr54hrqrdxhhjhnng.py
# Topologically Sorted Source Nodes: [to, to_1, add, to_4, add_2, pow_2, mean_1, add_3, rsqrt_1, mul_3, to_7, mul_4, to_6], Original ATen: [aten._to_copy, aten.add, aten.pow, aten.mean, aten.rsqrt, aten.mul]
# Source node to ATen node mapping:
#   add => add_12
#   add_2 => add_65
#   add_3 => add_78
#   mean_1 => mean_1
#   mul_3 => mul_52
#   mul_4 => mul_57
#   pow_2 => pow_2
#   rsqrt_1 => rsqrt_1
#   to => convert_element_type_2
#   to_1 => convert_element_type_3
#   to_4 => convert_element_type_12
#   to_6 => convert_element_type_14
#   to_7 => convert_element_type_15
# Graph fragment:
#   %convert_element_type_2 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mm, torch.float32), kwargs = {})
#   %convert_element_type_3 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%arg3_1, torch.float32), kwargs = {})
#   %add_12 : [num_users=3] = call_function[target=torch.ops.aten.add.Tensor](args = (%convert_element_type_2, %convert_element_type_3), kwargs = {})
#   %convert_element_type_12 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mm_2, torch.float32), kwargs = {})
#   %add_65 : [num_users=3] = call_function[target=torch.ops.aten.add.Tensor](args = (%convert_element_type_12, %add_12), kwargs = {})
#   %pow_2 : [num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%add_65, 2), kwargs = {})
#   %mean_1 : [num_users=1] = call_function[target=torch.ops.aten.mean.dim](args = (%pow_2, [-1], True), kwargs = {})
#   %add_78 : [num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%mean_1, 1e-05), kwargs = {})
#   %rsqrt_1 : [num_users=1] = call_function[target=torch.ops.aten.rsqrt.default](args = (%add_78,), kwargs = {})
#   %mul_52 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%add_65, %rsqrt_1), kwargs = {})
#   %convert_element_type_15 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%mul_52, torch.bfloat16), kwargs = {})
#   %mul_57 : [num_users=1] = call_function[target=torch.ops.aten.mul.Tensor](args = (%convert_element_type_15, %arg7_1), kwargs = {})
#   %convert_element_type_14 : [num_users=1] = call_function[target=torch.ops.prims.convert_element_type.default](args = (%add_65, torch.bfloat16), kwargs = {})
triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_2 = async_compile.triton('triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_2', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 8192, 'r0_': 8192},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*bf16', 'in_ptr2': '*bf16', 'in_ptr3': '*bf16', 'out_ptr1': '*bf16', 'out_ptr2': '*bf16', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]], (5,): [['tt.divisibility', 16]], (7,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_2', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 7, 'num_reduction': 1, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False}
)
@triton.jit
def triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_2(in_ptr0, in_ptr1, in_ptr2, in_ptr3, out_ptr1, out_ptr2, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    r0_numel = 5120
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    x0 = xindex
    _tmp10 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp0 = tl.load(in_ptr0 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp2 = tl.load(in_ptr1 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp4 = tl.load(in_ptr2 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp1 = tmp0.to(tl.float32)
        tmp3 = tmp2.to(tl.float32)
        tmp5 = tmp4.to(tl.float32)
        tmp6 = tmp3 + tmp5
        tmp7 = tmp1 + tmp6
        tmp8 = tmp7 * tmp7
        tmp9 = tl.broadcast_to(tmp8, [XBLOCK, R0_BLOCK])
        tmp11 = _tmp10 + tmp9
        _tmp10 = tl.where(r0_mask & xmask, tmp11, _tmp10)
    tmp10 = tl.sum(_tmp10, 1)[:, None]
    for r0_offset in range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp12 = tl.load(in_ptr0 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp14 = tl.load(in_ptr1 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp16 = tl.load(in_ptr2 + (r0_1 + 5120*x0), r0_mask & xmask, eviction_policy='evict_first', other=0.0).to(tl.float32)
        tmp27 = tl.load(in_ptr3 + (r0_1), r0_mask, eviction_policy='evict_last', other=0.0).to(tl.float32)
        tmp13 = tmp12.to(tl.float32)
        tmp15 = tmp14.to(tl.float32)
        tmp17 = tmp16.to(tl.float32)
        tmp18 = tmp15 + tmp17
        tmp19 = tmp13 + tmp18
        tmp20 = 5120.0
        tmp21 = (tmp10 / tmp20)
        tmp22 = 1e-05
        tmp23 = tmp21 + tmp22
        tmp24 = libdevice.rsqrt(tmp23)
        tmp25 = tmp19 * tmp24
        tmp26 = tmp25.to(tl.float32)
        tmp28 = tmp26 * tmp27
        tmp29 = tmp19.to(tl.float32)
        tl.store(out_ptr1 + (r0_1 + 5120*x0), tmp28, r0_mask & xmask)
        tl.store(out_ptr2 + (r0_1 + 5120*x0), tmp29, r0_mask & xmask)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/uk/cuk3p55hw27q7bm3ctnix5j5eaws3wrecrafniqghfgxmnaouzgr.py
# Topologically Sorted Source Nodes: [cat], Original ATen: [aten.cat]
# Source node to ATen node mapping:
#   cat => cat
# Graph fragment:
#   %cat : [num_users=1] = call_function[target=torch.ops.aten.cat.default](args = ([%sub_46, %add_161], -1), kwargs = {})
triton_poi_fused_cat_3 = async_compile.triton('triton_poi_fused_cat_3', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 33554432}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*i64', 'in_ptr2': '*bf16', 'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_cat_3', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 6, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_cat_3(in_ptr0, in_ptr1, in_ptr2, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = tl.full([XBLOCK], True, tl.int1)
    x0 = (xindex % 128)
    x1 = ((xindex // 128) % 32)
    x2 = xindex // 4096
    x4 = xindex
    tmp0 = x0
    tmp1 = tl.full([1], 0, tl.int64)
    tmp2 = tmp0 >= tmp1
    tmp3 = tl.full([1], 64, tl.int64)
    tmp4 = tmp0 < tmp3
    tmp5 = tl.load(in_ptr0 + (128*x1 + 6144*x2 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp6 = tl.load(in_ptr1 + (x2), tmp4, eviction_policy='evict_last', other=0.0)
    tmp7 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp8 = tmp6 + tmp7
    tmp9 = tmp6 < 0
    tmp10 = tl.where(tmp9, tmp8, tmp6)
    tl.device_assert(((0 <= tl.broadcast_to(tmp10, [XBLOCK])) & (tl.broadcast_to(tmp10, [XBLOCK]) < 1024000)) | ~(tmp4), "index out of bounds: 0 <= tl.broadcast_to(tmp10, [XBLOCK]) < 1024000")
    tmp12 = tl.load(in_ptr2 + (128*tmp10 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp13 = tmp5 * tmp12
    tmp14 = tl.load(in_ptr0 + (64 + 128*x1 + 6144*x2 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp15 = tl.load(in_ptr2 + (64 + 128*tmp10 + (x0)), tmp4, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp16 = tmp14 * tmp15
    tmp17 = tmp13 - tmp16
    tmp18 = tl.full(tmp17.shape, 0.0, tmp17.dtype)
    tmp19 = tl.where(tmp4, tmp17, tmp18)
    tmp20 = tmp0 >= tmp3
    tmp21 = tl.full([1], 128, tl.int64)
    tmp22 = tmp0 < tmp21
    tmp23 = tl.load(in_ptr0 + (64 + 128*x1 + 6144*x2 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp24 = tl.load(in_ptr1 + (x2), tmp20, eviction_policy='evict_last', other=0.0)
    tmp25 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp26 = tmp24 + tmp25
    tmp27 = tmp24 < 0
    tmp28 = tl.where(tmp27, tmp26, tmp24)
    tl.device_assert(((0 <= tl.broadcast_to(tmp28, [XBLOCK])) & (tl.broadcast_to(tmp28, [XBLOCK]) < 1024000)) | ~(tmp20), "index out of bounds: 0 <= tl.broadcast_to(tmp28, [XBLOCK]) < 1024000")
    tmp30 = tl.load(in_ptr2 + (128*tmp28 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp31 = tmp23 * tmp30
    tmp32 = tl.load(in_ptr0 + (128*x1 + 6144*x2 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp33 = tl.load(in_ptr2 + (64 + 128*tmp28 + ((-64) + x0)), tmp20, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp34 = tmp32 * tmp33
    tmp35 = tmp31 + tmp34
    tmp36 = tl.full(tmp35.shape, 0.0, tmp35.dtype)
    tmp37 = tl.where(tmp20, tmp35, tmp36)
    tmp38 = tl.where(tmp4, tmp19, tmp37)
    tl.store(out_ptr0 + (x4), tmp38, None)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/vp/cvpahabumyqw7a2g5b47qmyx6vbast55n6zlkvzuhjcvdq3azo4q.py
# Topologically Sorted Source Nodes: [cat_2], Original ATen: [aten.cat]
# Source node to ATen node mapping:
#   cat_2 => cat_1
# Graph fragment:
#   %cat_1 : [num_users=1] = call_function[target=torch.ops.aten.cat.default](args = ([%sub_63, %add_223], -1), kwargs = {})
triton_poi_fused_cat_4 = async_compile.triton('triton_poi_fused_cat_4', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 8388608}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*i64', 'in_ptr2': '*bf16', 'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_cat_4', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 6, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_cat_4(in_ptr0, in_ptr1, in_ptr2, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x0 = (xindex % 128)
    x1 = ((xindex // 128) % 8)
    x2 = xindex // 1024
    x4 = xindex
    tmp0 = x0
    tmp1 = tl.full([1], 0, tl.int64)
    tmp2 = tmp0 >= tmp1
    tmp3 = tl.full([1], 64, tl.int64)
    tmp4 = tmp0 < tmp3
    tmp5 = tl.load(in_ptr0 + (4096 + 128*x1 + 6144*x2 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp6 = tl.load(in_ptr1 + (x2), tmp4 & xmask, eviction_policy='evict_last', other=0.0)
    tmp7 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp8 = tmp6 + tmp7
    tmp9 = tmp6 < 0
    tmp10 = tl.where(tmp9, tmp8, tmp6)
    tl.device_assert(((0 <= tl.broadcast_to(tmp10, [XBLOCK])) & (tl.broadcast_to(tmp10, [XBLOCK]) < 1024000)) | ~(tmp4 & xmask), "index out of bounds: 0 <= tl.broadcast_to(tmp10, [XBLOCK]) < 1024000")
    tmp12 = tl.load(in_ptr2 + (128*tmp10 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp13 = tmp5 * tmp12
    tmp14 = tl.load(in_ptr0 + (4160 + 128*x1 + 6144*x2 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp15 = tl.load(in_ptr2 + (64 + 128*tmp10 + (x0)), tmp4 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp16 = tmp14 * tmp15
    tmp17 = tmp13 - tmp16
    tmp18 = tl.full(tmp17.shape, 0.0, tmp17.dtype)
    tmp19 = tl.where(tmp4, tmp17, tmp18)
    tmp20 = tmp0 >= tmp3
    tmp21 = tl.full([1], 128, tl.int64)
    tmp22 = tmp0 < tmp21
    tmp23 = tl.load(in_ptr0 + (4160 + 128*x1 + 6144*x2 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp24 = tl.load(in_ptr1 + (x2), tmp20 & xmask, eviction_policy='evict_last', other=0.0)
    tmp25 = tl.full([XBLOCK], 1024000, tl.int32)
    tmp26 = tmp24 + tmp25
    tmp27 = tmp24 < 0
    tmp28 = tl.where(tmp27, tmp26, tmp24)
    tl.device_assert(((0 <= tl.broadcast_to(tmp28, [XBLOCK])) & (tl.broadcast_to(tmp28, [XBLOCK]) < 1024000)) | ~(tmp20 & xmask), "index out of bounds: 0 <= tl.broadcast_to(tmp28, [XBLOCK]) < 1024000")
    tmp30 = tl.load(in_ptr2 + (128*tmp28 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp31 = tmp23 * tmp30
    tmp32 = tl.load(in_ptr0 + (4096 + 128*x1 + 6144*x2 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp33 = tl.load(in_ptr2 + (64 + 128*tmp28 + ((-64) + x0)), tmp20 & xmask, eviction_policy='evict_last', other=0.0).to(tl.float32)
    tmp34 = tmp32 * tmp33
    tmp35 = tmp31 + tmp34
    tmp36 = tl.full(tmp35.shape, 0.0, tmp35.dtype)
    tmp37 = tl.where(tmp20, tmp35, tmp36)
    tmp38 = tl.where(tmp4, tmp19, tmp37)
    tl.store(out_ptr0 + (x4), tmp38, xmask)
''', device_str='cuda')


# kernel path: /fp/projects01/ec12/mornil/vllm_cache/torch_compile_cache/509e891f09/rank_0_0/inductor_cache/az/caz77bz4cvy7r6h4a77i7mbvgnndm7kb4udhtgsontnwdav66oju.py
# Topologically Sorted Source Nodes: [view_4], Original ATen: [aten.view]
# Source node to ATen node mapping:
#   view_4 => full_default
# Graph fragment:
#   %full_default : [num_users=1] = call_function[target=torch.ops.aten.full.default](args = ([%arg1_1, 32, 128], 0.0), kwargs = {dtype: torch.bfloat16, layout: torch.strided, device: cuda:0, pin_memory: False})
triton_poi_fused_view_5 = async_compile.triton('triton_poi_fused_view_5', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 33554432}, 
    filename=__file__,
    triton_meta={'signature': {'out_ptr0': '*bf16', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=108, cc=80, major=8, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, warp_size=32), 'constants': {}, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_view_5', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'num_load': 0, 'num_reduction': 0, 'backend_hash': '47293E737FB461650F87749C5DACA1F6B144A22EE5CE7CD8757A23E028E91841', 'are_deterministic_algorithms_enabled': False, 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_view_5(out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = tl.full([XBLOCK], True, tl.int1)
    x0 = xindex
    tmp0 = 0.0
    tl.store(out_ptr0 + (x0), tmp0, None)
''', device_str='cuda')


async_compile.wait(globals())
del async_compile

def call(args):
    arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1, arg7_1, arg8_1, arg9_1, arg10_1 = args
    args.clear()
    s72 = arg1_1
    assert_size_stride(arg0_1, (s72, 32, 128), (4096, 128, 1))
    assert_size_stride(arg2_1, (5120, 4096), (4096, 1))
    assert_size_stride(arg3_1, (s72, 5120), (5120, 1))
    assert_size_stride(arg4_1, (5120, ), (1, ))
    assert_size_stride(arg5_1, (28672, 5120), (5120, 1))
    assert_size_stride(arg6_1, (5120, 14336), (14336, 1))
    assert_size_stride(arg7_1, (5120, ), (1, ))
    assert_size_stride(arg8_1, (6144, 5120), (5120, 1))
    assert_size_stride(arg9_1, (s72, ), (1, ))
    assert_size_stride(arg10_1, (1024000, 128), (128, 1))
    with torch.cuda._DeviceGuard(0):
        torch.cuda.set_device(0)
        buf0 = empty_strided_cuda((s72, 5120), (5120, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [linear], Original ATen: [aten.mm]
        extern_kernels.mm(reinterpret_tensor(arg0_1, (s72, 4096), (4096, 1), 0), reinterpret_tensor(arg2_1, (4096, 5120), (1, 4096), 0), out=buf0)
        del arg0_1
        del arg2_1
        buf2 = empty_strided_cuda((s72, 5120), (5120, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [to, to_1, add, pow_1, mean, add_1, rsqrt, mul, to_3, mul_1], Original ATen: [aten._to_copy, aten.add, aten.pow, aten.mean, aten.rsqrt, aten.mul]
        stream0 = get_raw_stream(0)
        triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_0.run(buf0, arg3_1, arg4_1, buf2, s72, 5120, stream=stream0)
        del arg4_1
        buf3 = empty_strided_cuda((s72, 28672), (28672, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [to, to_1, add, pow_1, mean, add_1, rsqrt, mul, to_3, mul_1, linear_1], Original ATen: [aten._to_copy, aten.add, aten.pow, aten.mean, aten.rsqrt, aten.mul, aten.mm]
        extern_kernels.mm(buf2, reinterpret_tensor(arg5_1, (5120, 28672), (1, 5120), 0), out=buf3)
        del arg5_1
        buf4 = empty_strided_cuda((s72, 14336), (14336, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [silu, mul_2], Original ATen: [aten.silu, aten.mul]
        triton_poi_fused_mul_silu_1_xnumel = 14336*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_mul_silu_1.run(buf3, buf4, triton_poi_fused_mul_silu_1_xnumel, stream=stream0)
        del buf3
        buf5 = buf2; del buf2  # reuse
        # Topologically Sorted Source Nodes: [silu, mul_2, linear_2], Original ATen: [aten.silu, aten.mul, aten.mm]
        extern_kernels.mm(buf4, reinterpret_tensor(arg6_1, (14336, 5120), (1, 14336), 0), out=buf5)
        del arg6_1
        del buf4
        buf7 = empty_strided_cuda((s72, 5120), (5120, 1), torch.bfloat16)
        buf12 = empty_strided_cuda((s72, 5120), (5120, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [to, to_1, add, to_4, add_2, pow_2, mean_1, add_3, rsqrt_1, mul_3, to_7, mul_4, to_6], Original ATen: [aten._to_copy, aten.add, aten.pow, aten.mean, aten.rsqrt, aten.mul]
        stream0 = get_raw_stream(0)
        triton_red_fused__to_copy_add_mean_mul_pow_rsqrt_2.run(buf5, buf0, arg3_1, arg7_1, buf7, buf12, s72, 5120, stream=stream0)
        del arg3_1
        del arg7_1
        del buf0
        del buf5
        buf8 = empty_strided_cuda((s72, 6144), (6144, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [to, to_1, add, to_4, add_2, pow_2, mean_1, add_3, rsqrt_1, mul_3, to_7, mul_4, linear_3], Original ATen: [aten._to_copy, aten.add, aten.pow, aten.mean, aten.rsqrt, aten.mul, aten.mm]
        extern_kernels.mm(buf7, reinterpret_tensor(arg8_1, (5120, 6144), (1, 5120), 0), out=buf8)
        del arg8_1
        del buf7
        buf9 = empty_strided_cuda((s72, 32, 128), (4096, 128, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [cat], Original ATen: [aten.cat]
        triton_poi_fused_cat_3_xnumel = 4096*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_cat_3.run(buf8, arg9_1, arg10_1, buf9, triton_poi_fused_cat_3_xnumel, stream=stream0)
        buf10 = empty_strided_cuda((s72, 8, 128), (1024, 128, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [cat_2], Original ATen: [aten.cat]
        triton_poi_fused_cat_4_xnumel = 1024*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_cat_4.run(buf8, arg9_1, arg10_1, buf10, triton_poi_fused_cat_4_xnumel, stream=stream0)
        del arg10_1
        del arg9_1
        buf11 = empty_strided_cuda((s72, 32, 128), (4096, 128, 1), torch.bfloat16)
        # Topologically Sorted Source Nodes: [view_4], Original ATen: [aten.view]
        triton_poi_fused_view_5_xnumel = 4096*s72
        stream0 = get_raw_stream(0)
        triton_poi_fused_view_5.run(buf11, triton_poi_fused_view_5_xnumel, stream=stream0)
    return (buf9, buf10, reinterpret_tensor(buf8, (s72, 8, 128), (6144, 128, 1), 5120), buf11, buf12, )


def benchmark_compiled_module(times=10, repeat=10):
    from torch._dynamo.testing import rand_strided
    from torch._inductor.utils import print_performance
    arg0_1 = rand_strided((8192, 32, 128), (4096, 128, 1), device='cuda:0', dtype=torch.bfloat16)
    arg1_1 = 8192
    arg2_1 = rand_strided((5120, 4096), (4096, 1), device='cuda:0', dtype=torch.bfloat16)
    arg3_1 = rand_strided((8192, 5120), (5120, 1), device='cuda:0', dtype=torch.bfloat16)
    arg4_1 = rand_strided((5120, ), (1, ), device='cuda:0', dtype=torch.bfloat16)
    arg5_1 = rand_strided((28672, 5120), (5120, 1), device='cuda:0', dtype=torch.bfloat16)
    arg6_1 = rand_strided((5120, 14336), (14336, 1), device='cuda:0', dtype=torch.bfloat16)
    arg7_1 = rand_strided((5120, ), (1, ), device='cuda:0', dtype=torch.bfloat16)
    arg8_1 = rand_strided((6144, 5120), (5120, 1), device='cuda:0', dtype=torch.bfloat16)
    arg9_1 = rand_strided((8192, ), (1, ), device='cuda:0', dtype=torch.int64)
    arg10_1 = rand_strided((1024000, 128), (128, 1), device='cuda:0', dtype=torch.bfloat16)
    fn = lambda: call([arg0_1, arg1_1, arg2_1, arg3_1, arg4_1, arg5_1, arg6_1, arg7_1, arg8_1, arg9_1, arg10_1])
    return print_performance(fn, times=times, repeat=repeat)


if __name__ == "__main__":
    from torch._inductor.wrapper_benchmark import compiled_module_main
    compiled_module_main('None', benchmark_compiled_module)
