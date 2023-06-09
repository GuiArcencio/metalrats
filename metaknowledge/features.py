from tsfresh.feature_extraction import EfficientFCParameters, MinimalFCParameters, ComprehensiveFCParameters

FEATURES = {
    "efficient": EfficientFCParameters(),
    "minimal": MinimalFCParameters(),
    "comprehensive": ComprehensiveFCParameters(),
    "catch22": None,
}