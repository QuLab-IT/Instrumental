from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Set
import json
import os

class ModelFeature(ABC):
    """Base class for model-specific features."""
    
    @abstractmethod
    def is_supported(self, model: str) -> bool:
        """Check if the feature is supported by the given model."""
        pass

class MultiChannelFeature(ModelFeature):
    """Feature mixin for multi-channel support."""
    
    def is_supported(self, model: str) -> bool:
        return model in ["33510B", "33512B", "33520B", "33522B", 
                        "33610A", "33612A", "33620A", "33622A"]

class ArbitraryWaveformFeature(ModelFeature):
    """Feature mixin for arbitrary waveform support."""
    
    def is_supported(self, model: str) -> bool:
        return model in ["33511B", "33512B", "33521B", "33522B",
                        "33611A", "33612A", "33621A", "33622A"]

class ModelCapabilities:
    """Class to manage model-specific capabilities."""
    
    def __init__(self, model: str):
        self.model = model
        self._features: Set[ModelFeature] = set()
        
    def add_feature(self, feature: ModelFeature) -> None:
        """Add a feature if it's supported by the model."""
        if feature.is_supported(self.model):
            self._features.add(feature)
            
    def has_feature(self, feature_type: type) -> bool:
        """Check if the model has a specific feature."""
        return any(isinstance(f, feature_type) for f in self._features)
    
    def get_features(self) -> Set[ModelFeature]:
        """Get all supported features."""
        return self._features.copy()

def generate_model_specific_code(model: str) -> str:
    """
    Generate model-specific code for the given model.
    
    Args:
        model: The model number (e.g., "33522B")
        
    Returns:
        str: Generated Python code for model-specific features
    """
    capabilities = ModelCapabilities(model)
    
    # Add known features
    capabilities.add_feature(MultiChannelFeature())
    capabilities.add_feature(ArbitraryWaveformFeature())
    
    # Generate code based on capabilities
    code = []
    
    # Add feature detection methods
    code.append("    def _check_dual_channel(self) -> bool:")
    code.append('        """Check if the model supports dual channel operation."""')
    code.append(f"        return {capabilities.has_feature(MultiChannelFeature).lower()}\n")
    
    code.append("    def _check_arbitrary_capability(self) -> bool:")
    code.append('        """Check if the model supports arbitrary waveforms."""')
    code.append(f"        return {capabilities.has_feature(ArbitraryWaveformFeature).lower()}\n")
    
    # Add validation methods for channel operations
    if capabilities.has_feature(MultiChannelFeature):
        code.append("    def _validate_channel(self, channel: int) -> None:")
        code.append('        """Validate channel number for dual-channel operations."""')
        code.append("        if channel not in [1, 2]:")
        code.append('            raise ValueError("Channel must be 1 or 2")')
        code.append("        if channel == 2 and not self._check_dual_channel():")
        code.append('            raise ValueError("Dual channel operation not available on this model")\n')
    
    # Add validation methods for arbitrary waveform operations
    if capabilities.has_feature(ArbitraryWaveformFeature):
        code.append("    def _validate_arbitrary_capability(self) -> None:")
        code.append('        """Validate arbitrary waveform capability."""')
        code.append("        if not self._check_arbitrary_capability():")
        code.append('            raise ValueError("Arbitrary waveform capability not available on this model")\n')
    
    return "\n".join(code) 